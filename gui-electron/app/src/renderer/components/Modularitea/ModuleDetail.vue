<template>
  <el-row>
  <el-col :span="24">
    <el-button icon="arrow-left" @click.native="backToHome">Kembali</el-button>
    <el-button type="primary" icon="arrow-right" @click.native="installModule">Pasang</el-button>
    <h3>{{ moduleDetail.name }}</h3>
    <p>{{ moduleDetail.description }}</p>
    <el-row>
      <el-col :span="4" v-for="(o, index) in moduleDetail.atoms" :key="o" :offset="index > 0 ? 2 : 0">
        <el-card :body-style="{ padding: '0px' }">
          <img src="" class="image">
          <div style="padding: 14px;">
            <span>{{ moduleDetail.atoms[index]}}</span>
            <div class="bottom clearfix">
              <time class="time"></time>
              <el-button type="text" class="button">Goto Website</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>

  </el-col>
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
      backToHome() {
        this.$router.push('/')
      },
      installModule() {
        // try exec
        let self = this
        var exec = require('child_process').exec;
        exec('node -v', function(error, stdout, stderr) {
            console.log('stdout: ' + stdout);
            self.$alert('This is a message' + stdout, 'Title', {
              confirmButtonText: 'OK',
              callback: action => {
                self.$message({
                  type: 'info',
                  message: `action: ${ action }`
                });
              }
            })
            console.log('stderr: ' + stderr);
            if (error !== null) {
                console.log('exec error: ' + error);
            }
        });

      }
    },
    mounted() {
      // get the root folder of electron project
      console.log('isi param : ', this.$route.params.folderName);
      let rootFolderElectron =  process.cwd();
      // goto parrent which is a truly root project
      let rootFolderProject = rootFolderElectron.substring(0, rootFolderElectron.lastIndexOf("/"));
      const moduleFolderPath = rootFolderProject + '/modules/' + this.$route.params.folderName;
      var modulePackage = JSON.parse(fs.readFileSync(moduleFolderPath + '/package.json', 'utf8'));
      this.moduleDetail = modulePackage.package
      console.log('isi package : ', modulePackage);
      console.log('isi package : ', this.moduleDetail);


    },
    data() {
      return {
        moduleDetail: {},
      }
    }
  }
</script>
<style scoped>
  a {
    color: rgb(50, 174, 110);
    text-decoration: none;
  }

  a:hover {
    color: rgb(40, 56, 76);
  }

  ul {
    list-style-type: none;
    margin-top: 10px;
  }

  li { display: inline-block; }
</style>
