<template>
    <div style="background:white; margin-bottom: 15px; padding: 0px;">
        <img class='image-show' 
            :src="props.src" 
            style=""
            lazy="true"
            fit='scale-down'
            alt="preview image" />
        <div class="description">
            <p class="content-description">{{ description }}</p>
            <p class="author-and-time" style="">{{ author }}</p>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { defineProps, onMounted } from 'vue';

const props = defineProps<{
    src: string,
    author: string,
    description: string
}>();

onMounted(() => {
    console.log(props.src)
})

// const emit = defineEmits([])

</script>

<style scoped>
.image-show {
    width: 100%;
    height: 200px;
    background: rgb(121, 17, 17);
    border: 0px; 
    margin: 0px; 
    padding: 0px;
}

.description {
    text-align: left;
    margin: 0px;
    border: 0px;
    padding: 0px;
}

.content-description {
    background: white;
    margin: 0px;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 5px;
    font-weight: bold;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    overflow: hidden;
    /*! autoprefixer: off */
    -webkit-box-orient: vertical;
    /*! autoprefixer: on */
    word-break: break-all;
}

.author-and-time {
    background: white;
    margin-top: 5px;
    padding-left: 10px;
    padding-right: 10px;
    padding-bottom: 5px;
}
</style>