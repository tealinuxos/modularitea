<template>
  <el-row :gutter="20">
    <el-col :span="8">
      <el-card :body-style="{ padding: '0px' }">
        <img src="../Modularitea/assets/icons/St.png" class="image">
        <div style="padding: 14px;">
          <span>Student</span>
          <div class="bottom clearfix">
            <time class="time"></time>
            <el-button type="text" class="button">Pilih</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
    <el-col :span="8">
      <el-card :body-style="{ padding: '0px' }">
        <img src="../Modularitea/assets/icons/UID.png" class="image">
        <div style="padding: 14px;">
          <span>User Interface Designer</span>
          <div class="bottom clearfix">
            <time class="time"></time>
            <el-button type="text" class="button">Pilih</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
    <el-col :span="8">
      <el-card :body-style="{ padding: '0px' }">
        <img src="../Modularitea/assets/icons/FeWD.png" class="image">
        <div style="padding: 14px;">
          <span>Front End Web Design</span>
          <div class="bottom clearfix">
            <time class="time"></time>
            <el-button type="text" class="button">Pilih</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    created () {
      // Set $route values that are not preset during unit testing
      if (process.env.NODE_ENV === 'testing') {
        this.$route = {
          name: 'landing-page',
          path: '/landing-page'
        }
      }
    },
    data() {
      return {
        input: ''
      }
    }
  }
</script>

<style scoped>
  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }
</style>
