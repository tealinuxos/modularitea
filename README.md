# Modularitea
Modularitea adalah proyek lanjutan dari [Tea Module Installer](https://github.com/tealinuxos/tea-module-installer), _installer_ modul-modul _development environments_ seperti (Fullstack Web, Front-end, Back-end, Mobile, Student, dll)) dengan membuatnya modular dan menggunakan GUI.

## Ide :
Membuat aplikasi _installer_ yang menyediakan _bundle development environment_ dengan konsep modular, hanya _install_ yang _developer_ butuhkan, misal seorang Back-end Web Developer membutuhkan _tech-stack_ Apache, PHP, MySql, PHPMyAdmin, Git dan Atom. Developer tersebut hanya perlu memilih _bundle Back-end Web Developer_ yang di inginkan dan klik install, semua yang tertera akan terinstall. Intinya adalah memudahkan _developer_ menyiapkan _development environment_-nya se-instan membuat mie instan.

Selayaknya mie instan, kamu bisa bisa memilih berbagai macam rasa :

1. Full-stack

    Mengandung :
   - [Apache2](https://httpd.apache.org/) - Webserver
   - [PHP 7](http://php.net)
   - [Composer](https://getcomposer.org/) -  Dependency Manager for PHP
   - [MySql](https://www.mysql.com/)
   - [PHPMyAdmin](https://www.phpmyadmin.net/) - Bringing MySQL to the web
   - [Atom](https://atom.io/) - A hackable text editor
   - [Git](https://git-scm.com/) - for Versioning Control
   - [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/) - Built for those who build the Web
2. Front-end
   - [NodeJS](https://nodejs.org)
   - [npm](https://www.npmjs.com/) - npm is the package manager for JavaScript
   - [Bower](https://bower.io/) - A package manager for the web
   - [Git](https://git-scm.com/) - for Versioning Control
   - [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/) - Built for those who build the Web
3. Back-end
   - [Apache2](https://httpd.apache.org/) - Webserver
   - [MongoDB](https://www.mongodb.com/)
4. Mobile
   - [Android Studio](https://developer.android.com/studio/index.html) - The Official IDE for Android
   - [SQLite Database Browser](http://sqlitebrowser.org/) - The Official home of the DB Browser for SQLite
5. Student
   - [Code::Block](http://www.codeblocks.org/) - Code::Blocks is a free C, C++ and Fortran IDE built to meet the most demanding needs of its users. It is designed to be very extensible and fully configurable.
   - [NetBeans](http://netbeans.org/)
   - gcc & g++
   - [Libre Office](https://www.libreoffice.org/)
6. Design
   - [InkScape](https://inkscape.org/) - for Draw vector freely
   - [GIMP](https://www.gimp.org/) - The Free & Open Source Image Editor
   - [Blender](https://www.blender.org/) - Open Source 3D creation. Free to use for any purpose, forever.
   - [Synfig](http://www.synfig.org/) - Open-source 2D animation software
7. Ada ide lain ?

## Latar belakang proyek ini dibuat :
Proyek ini meneruskan [Tea Module Installer](https://github.com/tealinuxos/tea-module-installer). Karena aplikasi installer tersebut hanya dapat berjalan di TeaLinuxOS, kami ingin installer ini bisa jalan di lintas distro Linux, sehingga lebih banyak _developer_ yang merasakan manfaatnya :).

Proyek ini juga terinspirasi dari [Laptop Script](https://github.com/thoughtbot/laptop) sebuah _script_ yang dapat merubah Mac menjadi mesin Web Development yang lengkap dan mudah.
## Rencana :

### Script : handle by [@mnirfan](https://github.com/mnirfan)
* Bash
* Python

### Front-end App : handle by [@dikyarga](https://github.com/dikyarga)
* [Electron](http://electron.atom.io/)
* HTML, CSS dan JavaScript
* [VueJS](http://vuejs.org/)
* [Element](http://element.eleme.io/)

### Design : handle by [@rezafaizarahman](https://github.com/rezafaizarahman)

## Cara ikut kontribusi :
* Usul ide atau lapor _bug_

    Cara cukup dengan membuat _issue_ pada repository ini / klik [tautan ini](https://github.com/tealinuxos/modularitea/issues/new) untuk jalan pintas.
* Berkontribusi di Kode
* Bantu buat dokumentasi yang lebih baik

## Lain-lain :
* Untuk pengguna yang masih bingung memilih _bundle_, bisa di refrensikan ke situs ini : [What is the best programming language for me?](http://www.bestprogramminglanguagefor.me)
* Setelah selesai memasang _bundle_ lalu di beri tutorial singkat ? di awali dengan memberi _overview_ tentang _tech stack_ yang dipilih.  
