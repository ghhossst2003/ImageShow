<template>
  <div class="chooseimage">
    <div class="bord-10">
      <div>
        <div class="block">
          <el-image class="thumb-image" :src="src" alt="">
            <template #placeholder>
              <div class="image-slot">Loading<span class="dot">...</span></div>
            </template>
          </el-image>
        </div>
      </div>

      <el-upload ref="uploadRef" class="upload" action="http://127.0.0.1:5000/upload_works" :auto-upload="false"
        :data="formData" :on-change="handleChange" :show-file-list="false" :limit="1" :on-exceed="handleExceed">
          <el-button type="primary" class="upload-button">select file</el-button><p>{{ filename }}</p>
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
  </div>
</template>

<script lang='ts' setup>
import { ref } from 'vue';
import type { UploadFile, UploadRawFile } from 'element-plus';
import type { UploadInstance } from 'element-plus';
import { genFileId } from 'element-plus';
import { onBeforeMount } from 'vue';
import axios from "axios";

interface AuthorData {
  id: number;
  name: string;
}
const uploadRef = ref<UploadInstance>()
const filename = ref('')
const description = ref('')
const author = ref('')
const src = ref("#")
const uploadFileRef = ref<UploadFile>()
const formData = ref<Record<string, any>>()
const authorOptions = ref<AuthorData[]>();

const handleExceed = (files: File[]) => {
  uploadRef.value!.clearFiles()
  const file = files[0] as UploadRawFile
  file.uid = genFileId()
  uploadRef.value!.handleStart(file)
}

const handleChange = (uploadFile: UploadFile) => {
  src.value = URL.createObjectURL(uploadFile.raw!)
  filename.value = uploadFile.name
  uploadFileRef.value = uploadFile
}

const onSubmit = () => {
  if (author.value == '') {
    console.log('Please choose creator!')
    return
  }
  if (description.value!.length == 0) {
    console.log("Please input description of the image!")
    return
  }
  let createTime: number = new Date().getTime()
  formData.value = {
    'creation_time': createTime,
    'author': author.value!,
    'description': description.value!,
  }
  uploadRef.value!.submit()
}

onBeforeMount(() => {
  axios.get("http://127.0.0.1:5000/authors").then((response: { data: any; }) => {
    let da = eval(response.data);
    authorOptions.value = da['data']
  })
})

</script>

<style scoped>
.block {
  width: 100%;
  height: 300px;
}

.thumb-image {
  width: 100%;
  height: 100%;
}

.image-image {
  width: 100%;
  height: 100%;
  min-width: 100%;
  min-height: 300;
}

.chooseimage {
  width: 100%;
  display: inline-block;
  margin: 0px;
  border: 0px;
  padding: 0px;
  background: bisque;
}

.upload {
  text-align: center;
  align-items: center;
  margin-top: 10px;
  margin-bottom: 10px;
}

.upload-button {
  width: 100%;
}

.m-2 {
  width: 100%;
}

.submit-info {
  width: 100%;
  margin-top: 10px;
}

.bord-10 {
  padding: 10px;
}
</style>