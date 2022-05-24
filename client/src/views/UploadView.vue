<template>
  <div class="upload">
    <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
    <ChooseImage />
  </div>
</template>

<script>
import ChooseImage from '@/components/ChooseImage.vue'

export default {
  name: "UpLoad",
  components: {
      ChooseImage
    }
};


</script>
