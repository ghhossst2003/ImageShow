<template>
  <div class="chooseimage">
    <div>
      <div class="block">
        <el-image class="thumb-image" :src="src" alt="">
          <template #placeholder>
            <div class="image-slot">Loading<span class="dot">...</span></div>
          </template>
        </el-image>
      </div>
    </div>
    <p>{{ filename }}</p>
    <el-upload ref="uploadRef" class="upload" action="http://127.0.0.1:5000/upload_works" 
      :auto-upload="false" 
      :data="formData"
      :on-change="handleChange" 
      :show-file-list="false" 
      :limit="1" 
      :on-exceed="handleExceed">
      <el-button type="primary" class="upload">select file</el-button>
    </el-upload>
    <div class="infor">
      <el-select v-model="author" class="m-2" placeholder="Select Author" size="large">
        <el-option v-for="item in authorOptions" :key="item.id" :label="item.name" :value="item.id" />
      </el-select>
      <el-input v-model="description" class="submit-info" :rows="10" type="textarea"
        placeholder="Please input description" />
      <el-button type="primary" class="submit-info" @click="onSubmit">submit</el-button>
    </div>
  </div>
</template>

<script lang='ts' setup>
import { ref } from 'vue';
import type { UploadFile, UploadRawFile } from 'element-plus';
import type { UploadInstance } from 'element-plus';
import { genFileId } from 'element-plus';
import { onBeforeMount } from 'vue';
import axios from "axios";

const uploadRef = ref<UploadInstance>()
const filename = ref('')
const description = ref('')
const author = ref('')
const src = ref("#")
const uploadFileRef = ref<UploadFile>()
const fileRef = ref<File>()
const formData = ref<Record<string, any>>()

const handleExceed = (files: File[]) => {
  console.log('file:', files[0])
  fileRef.value = files[0] as UploadRawFile
  uploadRef.value!.clearFiles()
  const file = files[0] as UploadRawFile
  file.uid = genFileId()
  uploadRef.value!.handleStart(file)
}

const handleChange = (uploadFile: UploadFile) => {
  src.value = URL.createObjectURL(uploadFile.raw!)
  filename.value = uploadFile.name
  uploadFileRef.value = uploadFile
  console.log('handle change:', uploadFile)
}

const authorOptions = ref([]);

const onSubmit = () => {
  console.log(author.value)
  console.log('123', uploadFileRef.value!)
  if (author.value == '') {
    console.log('请选择创作者。')
    return
  }
  if (description.value!.length == 0) {
    console.log("请输入描述。")
    return
  }
  let createTime: number = new Date().getTime()
  formData.value = {
    'creation_time': createTime,
    'author': author.value!,
    'description': description.value!
  }

  // let config = {
  //   headers: {
  //     'Content-Type': 'multipart/form-data'
  //   }
  // }
  console.log('uploadRef:', uploadRef.value)
  uploadRef.value!.submit()
  // axios({
  //   method: 'post',
  //   url: 'http://127.0.0.1:5000/upload_works',
  //   data: formData,
  //   headers: headers
  // });
  // console.log(formData)
  // axios.post("http://127.0.0.1:5000/upload_works", formData, config).then((response) => {
  //   console.log(response)
  // }).catch((error) => {
  //   console.log(error)
  // })
}

onBeforeMount(() => {
  console.log("fdfafdafad")
  axios.get("http://127.0.0.1:5000/authors").then((response: { data: any; }) => {
    let da = eval(response.data);
    console.log(response.data);
    authorOptions.value = da['data']
  })
})

</script>

<style scoped>
.block {
  width: 100%;
  height: 400px;
}

.thumb-image {
  width: 100%;
  height: 400px;
}

.image-image {
  width: 100%;
  height: 400px;
  min-width: 100%;
  min-height: 300;
}

.chooseimage {
  width: 600px;
  display: inline-block;
  margin: 10px;
  background: bisque;
}

.upload {
  width: 100%;
}

.m-2 {
  width: 100%;
  margin-top: 10px;
}

.submit-info {
  width: 100%;
  margin-top: 10px;
}
</style>