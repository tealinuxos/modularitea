<template>
  <el-row>
  <el-col :span="30">
    <el-button type="primary" icon="arrow-left"  @click.native="backToHome" >Kembali</el-button>
    
    <br/>
    <br/>
    <el-card  class="box-card" >
      
      <div slot="header" class="clearfix">
        <span style="line-height: 36px;font-size:20px;font-weight:bold">{{ moduleDetail.name }}</span>
        <el-button type="warning" icon="el-icon-download" style="float: right;text-align:center;font-weight:bold" @click.native="installModule"><i class="el-icon-check"> Pasang</i></el-button>
        <!-- <el-button style="float: right;" type="primary">Operation button</el-button> -->
      </div>
      <div class="clearfix">
        <el-tabs type="border-card">
        <el-tab-pane :label="o.name" v-for="(o, index) in atoms" :key="index" tab-position="left">
          <div class="desc">
            <h3 class="desc">Deskripsi : </h3>
             <p class="desc">{{o.description}}</p>
             <h3 class="desc">Pengembang : </h3>
             <p class="desc">{{o.pengembang}}</p>
             <h3 class="desc">Rilis perdana : </h3>
             <p class="desc">{{o.rilisperdana}}</p>
             <h3 class="desc">Rilis Stabil : </h3>
             <p class="desc">{{o.rilisstabil}}</p>
             <h3 class="desc">Repositori : </h3>
             <p class="desc">{{o.repositori}}</p>
             <h3 class="desc">Bahasa Pemograman : </h3>
             <p class="desc">{{o.bahasapemrograman}}</p>
             <h3 class="desc">Sistem Operasi : </h3>
             <p class="desc">{{o.sistemoperasi}}</p>
          </div>
        </el-tab-pane>
      </el-tabs>

      </div>
    </el-card>
  </el-col>
</el-row>
</template>
<script>
  import fs from 'fs'
  var os = require("os");
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
        let command = "xterm -e /usr/bin/modularitea-cli.py --module=" + this.$route.params.folderName
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
            case (error == null):
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
      //get username
      const username = process.env.USER;
      // get the root folder of electron project
      console.log('isi param : ', this.$route.params.folderName);
      // get the root folder of electron project
      
      // Ketika akan build aktifkan var dibawa ini
      // let moduleFolderPath = '/usr/share/modularitea-package/modules/' + this.$route.params.folderName;
      // let atomsFolderPath = '/usr/share/modularitea-package/atoms/';

      // Ketika mode devloper aktifkan var dibawa ini, ganti rizkirf dengan username kalian
      let moduleFolderPath = '/home/rizkirf/Desktop/modularitea/modules/' + this.$route.params.folderName;
      let atomsFolderPath = '/home/rizkirf/Desktop/modularitea/atoms/';

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
        tabPos:'left',
        atoms: []
      }
    }
  }
</script>
<style scoped>
  a {
    color: rgb(50, 174, 110);
    text-decoration: none;
    transition:.2s;
  }

  a:hover {
    color: rgb(40, 56, 76);
  }

  ul {
    list-style-type: none;
    margin-top: 10px;
  }

  li { display: inline-block; }

  .title{
    font-family: sans-serif;
  }

  *{
    color: white;
    font-family: sans-serif;
  }
  .box-card{
    background:rgb(8, 170, 143);
  }
  .desc{
    color:#333;
  }

  .btn-kembali{
    background: rgb(50, 174, 110);
  }

  .btn-kembali:hover{
    transition: .2s;
    background: rgb(40, 56, 76);
  }
</style>
