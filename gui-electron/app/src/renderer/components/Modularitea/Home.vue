<template>
  <el-row :gutter="20">
    <el-col :span="8" v-for="module in modules">
      <el-card :body-style="{ padding: '0px' }">
        <img :src="getPic(module.package.folderName)" class="image">
        <!-- <img src="../../../../../../modules/Student/icon.png" alt=""> -->
        <!-- <img :src="require('../../../../../../modules/'+  module.package.icon + '/icon.png')" class="image"> -->
        <div style="padding: 14px;">
          <h3>{{module.package.name}}</h3>
          <div class="bottom clearfix">
            <p>{{module.package.description}}</p>
            <el-button type="primary" @click.native="gotoModuleDetail(module.package.folderName)">Pilih</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
    <!-- {{ modules }} -->
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
      },
      gotoModuleDetail(folderName) {
        this.$router.push('/module/' + folderName)
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
          // if icons, skip
          if (file != 'icons') {
            // get package.json of the module
            var modulePackage = JSON.parse(fs.readFileSync(modulesFolderPath + '/' + file + '/package.json', 'utf8'));
            // add icon path property
            modulePackage.package.folderName = file
            modulePackage.package.icon = '../../../../../../modules/Student/icon.png'
            this.modules.push(modulePackage)
          }
        });
      })

      // try exec
      var exec = require('child_process').exec;
      exec('node -v', function(error, stdout, stderr) {
          console.log('stdout: ' + stdout);
          console.log('stderr: ' + stderr);
          if (error !== null) {
              console.log('exec error: ' + error);
          }
      });

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
