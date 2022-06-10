<template>
  <el-container>
    <el-header class="header-fix" ref="headerRef">
      head
    </el-header>
    <el-container>
      <el-aside width="200px" ref="asideRef" v-show="asideShowRef">Aside</el-aside>
      <el-main ref="mainContentRef" style="width: 100%; padding: 0px">
        <ImageItem class='image-item' v-for="item in imageListRef" :key="item.id" :src="config.imageServer + item.path"
          :author="item.name" :description="item.description"></ImageItem>
      </el-main>
    </el-container>
  </el-container>
</template>

<script lang="ts" setup>
import ImageItem from "../components/ImageItem.vue";
import { nextTick, onBeforeMount, onBeforeUnmount, onMounted, ref } from "vue";
import axios from "axios";
import config from "../assets/config";

const requestPage = ref(1)
const imageSrcRef = ref("")
imageSrcRef.value = require("../static/logo.png")
const headerRef = ref()
const mainContentRef = ref()
const mainContentHeightRef = ref()
const asideRef = ref()
const asideShowRef = ref(false)
const isLoading = ref(false)
const isLoadFinish = ref(false)

interface item {
  id: number;
  description: string;
  creation_time: number;
  upload_time: number;
  path: string;
  name: string
}
const imageListRef = ref<Array<item>>()


// onBeforeMount(() => {
//   axios.get(config.url.getWorksForPage+requestPage.value!).then((response: { data: any; }) => {
//     let rsp = eval(response.data)
//     console.log(rsp['data'])
//     imageListRef.value = rsp['data']
//   })
// })


const getImageList = (url: string): any => {
  axios.get(url).then((response: { data: any; }) => {
    let rsp = eval(response.data)
    if (imageListRef.value == undefined) {
      imageListRef.value = rsp['data']
    } else {
      imageListRef.value = imageListRef.value!.concat(rsp['data'])
      console.log("image list length:", imageListRef.value!.length) //去掉一下测试
    }
    if (rsp['data'].length != 0) {
      requestPage.value!++
    } else {
      isLoadFinish.value = true
    }
  }).finally(()=>{
    isLoading.value! = false
   })
}


onBeforeMount(() => {
  const url = config.url.getWorksForPage + requestPage.value!
  getImageList(url)
})

const handleScroll = (ev: Event) => {
  const mainContent = ev.target as HTMLElement
  console.log("requestPage.value!:", requestPage.value!)
  if ((mainContent.scrollHeight - (mainContent.clientHeight + mainContent.scrollTop)) < 300
    && (!(isLoading.value!)) &&(!(isLoadFinish.value!))) {
    isLoading.value! = true
    const url = config.url.getWorksForPage + requestPage.value!
    getImageList(url)
  }
}

onMounted(() => {
  console.log(headerRef.value!.$el.clientHeight)
  let headElement = headerRef.value!.$el as HTMLElement
  mainContentHeightRef.value = document.documentElement.clientHeight - headElement.clientHeight
  mainContentRef.value!.$el.style.height = document.documentElement.clientHeight - headElement.offsetHeight + 'px'
  window.onresize = () => {
    // 通过捕获系统的onresize事件触发我们需要执行的事件
    let headElement = headerRef.value!.$el as HTMLElement
    mainContentRef.value!.$el.style.height = document.documentElement.clientHeight - headElement.offsetHeight + 'px'
    if (document.documentElement.clientWidth > 750) {
      asideShowRef.value = true
    } else {
      asideShowRef.value = false
    }
  }
  nextTick(() => {
    const mainContent = mainContentRef.value!.$el as HTMLElement
    mainContent.addEventListener('scroll', handleScroll)
  })
})

onBeforeUnmount(() => {
  const mainContent = mainContentRef.value!.$el as HTMLElement
  mainContent.removeEventListener('scroll', handleScroll)
})


</script>

<style>
.el-container {
  margin: 0px;
  padding: 0px;
  height: 100px;
}

.header-fix {
  width: 100%;
  background: blue;
}

.el-aside {
  background: gold;
}

.el-main {
  background: RGB(249, 249, 249);
  width: 100%;
  height: 200px;
}

.image-item {
  margin-top: 0px;
  padding: 0px;
  width: 100%;
  height: 250px;
}
</style>