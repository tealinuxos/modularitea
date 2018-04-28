<template>
  <el-row>
    <el-col :span="24"><div class="grid-content bg-purple"><Home></Home></div></el-col>
  </el-row>
</template>

<script>
  import Home from './Modularitea/Home'

  export default {
    components: {
      Home
    },
    name: 'landing-page',
  }
</script>

<style scoped>
  img {
    margin-top: -25px;
    width: 450px;
  }
</style>
