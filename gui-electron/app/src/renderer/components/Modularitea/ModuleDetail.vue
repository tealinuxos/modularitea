<template>
  <el-row>
  <el-col :span="24">
    <el-button icon="arrow-left" @click.native="backToHome">Kembali</el-button>
    <el-button type="primary" icon="arrow-right" @click.native="installModule">Pasang</el-button>
    <h3>{{ moduleDetail.name }}</h3>
    <p>{{ moduleDetail.description }}</p>
    <el-row>
      <el-col :span="4" v-for="(o, index) in atoms" :key="o">
        <el-card :body-style="{ padding: '0px' }">
          <img src="" class="image">
          <div style="padding: 14px;">
            <span>{{ atoms[index].name }}</span>
            <p>{{ atoms[index].description }}</p>
            <div class="bottom clearfix">
              <time class="time"></time>
              <el-button type="text" class="button"  @click.native="gotoHomepage(atoms[index].homepage)">Goto Homepage</el-button>
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
  const shell = require('electron').shell;

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
        let command = "x-terminal-emulator -e /usr/local/bin/modularitea-cli --module=" + this.$route.params.folderName
        exec('gksu "' + command + '"', function(error, stdout, stderr) {
            console.log('stdout: ' + stdout);

            console.log('stderr: ' + stderr);
            if (error !== null) {
                console.log('exec error: ' + error);
            }
        }).on('exit', code => {
          let message = ''
          switch (code) {
            case 0:
              message = 'Selamat kamu berhasil memesang modul ' + this.$route.params.folderName
              break;
            default:

          }

          self.$alert(message, 'Sukses', {
            confirmButtonText: 'OK',
            callback: action => {
              self.$message({
                type: 'success',
                message: `action: ${ action }`
              });
            }
          })
        });
      },
      gotoHomepage(homepageUrl) {
        shell.openExternal(homepageUrl)
      }
    },
    mounted() {
      // get the root folder of electron project
      console.log('isi param : ', this.$route.params.folderName);
      let rootFolderElectron =  process.cwd();
      // goto parrent which is a truly root project
      let rootFolderProject = rootFolderElectron.substring(0, rootFolderElectron.lastIndexOf("/"));
      let moduleFolderPath = rootFolderProject + '/modules/' + this.$route.params.folderName;
      let atomsFolderPath = rootFolderProject + '/atoms/'

      var modulePackage = JSON.parse(fs.readFileSync(moduleFolderPath + '/package.json', 'utf8'));
      this.moduleDetail = modulePackage.package
      for (var i = 0; i < modulePackage.package.atoms.length; i++) {
        var atomDetailPackage = JSON.parse(fs.readFileSync(atomsFolderPath + modulePackage.package.atoms[i] + '/package.json', 'utf8'));
        this.atoms.push(atomDetailPackage.package)
      }
    },
    data() {
      return {
        moduleDetail: {},
        atoms: []
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
