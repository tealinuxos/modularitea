<template>
  <el-row :gutter="20">
    <el-col :span="6" v-for="module1 in modules">
      <el-card :body-style="{ padding: '0px' }">
        <img :src="getPic(module1.package.folderName)" class="image">
        <!-- <img src="../../../../../../modules/Student/icon.png" alt=""> -->
        <!-- <img :src="require('../../../../../../modules/'+  module.package.icon + '/icon.png')" class="image"> -->
        <div style="padding: 14px;">
          <h3>{{module1.package.name}}</h3>
          <div class="bottom clearfix">
            <p>{{module1.package.description}}</p>
            <el-button type="primary" @click.native="gotoModuleDetail(module1.package.folderName)">Pilih</el-button>
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
        var images = require.context('../../../../../../icons/', false, /\.png$/)
        return images('./' + folderName + '.png')
      },
      gotoModuleDetail(folderName) {
        this.$router.push('/module/' + folderName)
      }

    },
    mounted() {
      // get the root folder of electron project
      let rootFolderElectron =  process.cwd();
      let rootFolderProject1 = rootFolderElectron.substring(0, rootFolderElectron.lastIndexOf("/"));
      // let rootFolderProject2 = rootFolderProject1.substring(0, rootFolderProject1.lastIndexOf("/"));
      // let rootFolderProject3 = rootFolderProject2.substring(0, rootFolderProject2.lastIndexOf("/"));
      
      const modulesFolderPath = rootFolderProject1 + '/modules';

      fs.readdir(modulesFolderPath, (err, files) => {
        if (err) {
          throw err;
        }
        files.forEach(file => {
          console.log('nama folder nya apa aja  ', file);
          // if icons, skip
          if (file != 'icons') {
            // get package.json of the module
            var modulePackage = JSON.parse(fs.readFileSync(modulesFolderPath + '/' + file + '/package.json', 'utf8'));
            // add icon path property
            modulePackage.package.folderName = file
            // modulePackage.package.icon = '../../../../../../modules/Student/icon.png'
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
  .el-col {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
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
