<template>
  <el-row>
  <el-col :span="24">
    <el-button icon="arrow-left" @click.native="backToHome">Kembali</el-button>
    <br/>
    <br/>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span style="line-height: 36px;">{{ moduleDetail.name }}</span>
        <el-button type="primary" icon="arrow-right" style="float: right;" @click.native="installModule">Pasang</el-button>
        <!-- <el-button style="float: right;" type="primary">Operation button</el-button> -->
      </div>
      <div class="clearfix">
        <h3 class="title">Komposisi :</h3>
        <el-collapse  v-for="(o, index) in atoms" :key="index">
            <el-collapse-item :title="o.name" :name="index">
              <div>{{o.description}}</div>
              <div class="">
                <el-button type="text" class="button"  @click.native="gotoHomepage(atoms[index].homepage)">Goto Homepage</el-button>
              </div>
            </el-collapse-item>
        </el-collapse>
      </div>
    </el-card>
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
        var images = require.context('../../../../../../icons/', false, /\.png$/)
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
        let errorMessage = ''
        exec('gksu "' + command + '"', function(error, stdout, stderr) {
            console.log('stdout: ' + stdout);

            console.log('stderr: ' + stderr);
            if (error !== null) {
              self.$alert('Instalasi module ' + self.$route.params.folderName + ' gagal, karena : ' + error, 'Gagal install modul ):', {
                confirmButtonText: 'OK',
                callback: action => {
                  self.$message({
                    type: 'error',
                    message: `Jika belum terselesaikan masalahnya, silahkan hubungi developer TeaLinuxOS di tealinuxos.org (:`
                    });
                  }
                })
                console.log('exec error: ' + error);
            }
        }).on('exit', code => {
          let message = ''
          switch (true) {
            case (code == 0):
              message = 'Selamat kamu berhasil memesang modul ' + this.$route.params.folderName
              self.$alert(message, 'Sukses install modul!', {
                confirmButtonText: 'OK',
                callback: action => {
                  self.$message({
                    type: 'success',
                    message: `Selamat menikmati racikan kami (:`
                    });
                  }
                })
              break;
            default:

          }

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
