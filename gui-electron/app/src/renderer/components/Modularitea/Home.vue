<template>
  <el-row :gutter="20">
    <el-col :span="8" v-for="module in modules">
      <el-card :body-style="{ padding: '0px' }">
        <p>{{module.package.folderName}}</p>
        <img :src="getPic(module.package.folderName)">
        <!-- <img src="../../../../../../modules/Student/icon.png" alt=""> -->
        <!-- <img :src="require('../../../../../../modules/'+  module.package.icon + '/icon.png')" class="image"> -->
        <div style="padding: 14px;">
          <span>{{module.package.name}}</span>
          <div class="bottom clearfix">
            <time class="time">{{module.package.description}}</time>
            <el-button type="text" class="button">Pilih</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
    {{ modules }}
  </el-row>

</template>

<script>
  import fs from 'fs'
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
    methods: {
      getPic(folderName) {
        var images = require.context('../../../../../../modules/icons/', false, /\.png$/)
        return images('./' + folderName + '.png')
      }
    },
    mounted() {
      // get the root folder of electron project
      let rootFolderElectron =  process.cwd();
      // goto parrent which is a truly root project
      let rootFolderProject = rootFolderElectron.substring(0, rootFolderElectron.lastIndexOf("/"));
      const modulesFolderPath = rootFolderProject + '/modules';

      fs.readdir(modulesFolderPath, (err, files) => {
        if (err) {
          throw err;
        }
        files.forEach(file => {
          // get package.json of the module
          var modulePackage = JSON.parse(fs.readFileSync(modulesFolderPath + '/' + file + '/package.json', 'utf8'));
          // add icon path property
          modulePackage.package.folderName = file
          modulePackage.package.icon = '../../../../../../modules/Student/icon.png'
          this.modules.push(modulePackage)
        });
      })
    },
    data() {
      return {
        input: '',
        modules: []
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
