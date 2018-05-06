<template>

  <el-row :gutter="5">
    <el-carousel :interval="4000" type="card" height="400px">
      <el-carousel-item v-for="item in modules" :key="item" class="el-car-item">
        <img :src="getPic(item.package.folderName)" class="img-carousel">
      </el-carousel-item>
    </el-carousel>

    <el-col :xs="12" :sm="8" :md="4" v-for="module1 in modules" style="height:580px;">
      <el-card :body-style="{ padding: '0px', margin:'0' }">
        <img :src="getPic(module1.package.folderName)" class="image">
        <!-- <img src="../../../../../../modules/Student/icon.png" alt=""> -->
        <!-- <img :src="require('../../../../../../modules/'+  module.package.icon + '/icon.png')" class="image"> -->
        <div style="padding: 10px;">
          <div class="block">
            <span class="demonstration">Level : </span>
            <el-rate v-model="module1.package.level"></el-rate>
          </div>
          <h3>{{module1.package.name}}</h3>
          <div class="clearfix">
            <p>{{module1.package.description}}</p>
            <el-button  type="primary" @click.native="gotoModuleDetail(module1.package.folderName)">Pilih</el-button>
          </div>
          
        </div>
      </el-card>
    </el-col>
    <!-- {{ modules }} -->
  </el-row>


</template>

<script>
  var os = require("os")
  import fs from 'fs'
  export default {
    data() {
      return {
        input: '',
        modules: [],
        items: []
      }
    },
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
        this.fullscreenLoading = true;
       
          this.$router.push('/module/' + folderName)
        
        
      }

    },
    mounted() {
      // get username
      const username = process.env.USER;
      // get the root folder of electron project
      let rootFolderElectron =  process.cwd();
      let rootFolderProject1 = rootFolderElectron.substring(0, rootFolderElectron.lastIndexOf("/"));
      // let rootFolderProject2 = rootFolderProject1.substring(0, rootFolderProject1.lastIndexOf("/"));
      // let rootFolderProject3 = rootFolderProject2.substring(0, rootFolderProject2.lastIndexOf("/"));
      
      // Ketika akan build aktifkan var dibawa ini
      // const modulesFolderPath ='/usr/share/modularitea-package/modules/';
      
      // Ketika mode devloper aktifkan var dibawa ini, ganti rizkirf dengan username kalian
      const modulesFolderPath ='/home/rizkirf/Desktop/modularitea/modules/';
      
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
            this.items.push(modulePackage.package.icon)
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

    }
  }
</script>

<style scoped>
  *{
    font-family: sans-serif;
  }
  p{
    margin-top: -5px;
    line-height: .25in;
  }
  .img-carousel
  {
    height: 100%;
    width: 100%;
  }
  .el-car .el-car-item{
    height: 2000px;
  }
  h3{
    color:rgb(28, 116, 231);
  }
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
    margin-top: 5px;
    line-height: 12px;
  }

  .el-button  {
    width: 100%;
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
