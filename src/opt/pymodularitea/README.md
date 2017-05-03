# Modularitea
Modularitea merupakan aplikasi yang dapat memasang lingkungan kerja untuk para pengembang hanya dengan beberapa langkah sederhana. Modularitea menyederhanakan proses cari, unduh, pasang dan ubahsuai  ke dalam bentuk [modul](#modul).

Sebelumnya, Developer [TeaLinuxOS](http://tealinuxos.org) telah membuat nutrisi berbentuk [Tea Module Installer](https://github.com/tealinuxos/tea-module-installer). Namun, Tea Module Installer hanya dapat berjalan di TeaLinuxOS. Modularitea dibuat agar Tea Module Installer dapat berjalan lintas distro Linux. Modularitea juga terinspirasi dari script [laptop](https://thoughtbot.com/tools) buatan [Thoughtbot](https://thoughtbot.com/), script tersebut dapat secara otomatis memasang lingkungan kerja pengembang Web di platform Mac.

## Konsep Modularitea

### Atom
Pada Modularitea, aplikasi untuk pengembang seperti IDE, editor teks dan script diberi istilah Atom. Atom merupakan bagian terkecil yang ada pada Modularitea.

### Modul
Untuk mengembangkan aplikasi, para pengembang membutuhkan lebih dari satu Atom. Karena itu Atom dikumpulkan kedalam satu wadah yang disebut Modul.

### Kandungan Modul
Di dunia terdapat berbagai macam tipe pengembang, Modularitea ada untuk menyediakan berbagai macam modul yang telah disesuaikan dengan tipe-tipe pengembang tersebut. Modul yang disediakan terdiri dari berbagai macam rasa:

#### 1. Full-stack Web Developer (FsWD).
Tipe pengembang ini akan berhubungan dengan aplikasi web dari awal hingga akhir.
Modul ini mengandung:
- apt [Apache2](https://httpd.apache.org/) - Webserver
- apt [PHP 7](http://php.net) - a server scripting language
- apt [Composer](https://getcomposer.org/) -  Dependency Manager for PHP
- apt [MySql](https://www.mysql.com/) - a database system used on the web
- apt [PHPMyAdmin](https://www.phpmyadmin.net/) - Bringing MySQL to the web
- deb [Atom](https://atom.io/) - A hackable text editor
- apt [Git](https://git-scm.com/) - for Versioning Control
- apt [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/) - Built for those who build the Web

#### 2. Front-end Web Developer (FeWD)
Tipe pengembang ini akan berhubungan dengan antarmuka tampilan web.
- apt [NodeJS](https://nodejs.org) -  is an open-source, cross-platform JavaScript runtime environment for developing a diverse variety of tools and applications
- apt [Npm](https://www.npmjs.com/) - npm is the package manager for JavaScript
- script [Bower](https://bower.io/) - A package manager for the web
- apt [Git](https://git-scm.com/) - for Versioning Control
- apt [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/) - Built for those who build the Web

#### 3. Back-end Web Developer (BeWD)
Tipe pengembang ini akan berhubungan dengan server dan database web.
- apt [Apache2](https://httpd.apache.org/) - Webserver
- apt [PHP 7](http://php.net) - a server scripting language
- apt [Composer](https://getcomposer.org/) -  Dependency Manager for PHP
- apt [MySql](https://www.mysql.com/) - a database system used on the web
- apt [PHPMyAdmin](https://www.phpmyadmin.net/) - Bringing MySQL to the web
- apt [Git](https://git-scm.com/) - for Versioning Control
- apt [MongoDB](https://www.mongodb.com/) - an open-source document database and leading NoSQL database
- apt [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/) - Built for those who build the Web
- apt [NodeJS](https://nodejs.org) -  is an open-source, cross-platform JavaScript runtime environment for developing a diverse variety of tools and applications
- apt [Npm](https://www.npmjs.com/) - npm is the package manager for JavaScript

#### 4. Mobile Android Developer (MAD)
Tipe pengembang ini akan berhubungan dengan pengembangan aplikasi mobile Android.
- zip [Android Studio](https://developer.android.com/studio/index.html) - The Official IDE for Android
- apt [SQLite Database Browser](http://sqlitebrowser.org/) - The Official home of the DB Browser for SQLite
- apt [Git](https://git-scm.com/) - for Versioning Control

#### 5. User Interface Designer (UID)
Tipe pengembang ini akan berhubungan dengan desain antarmuka, baik web, mobile maupun destop.
- apt [Inkscape](https://inkscape.org/) - for designing User Interface
- deb [Pencil](http://pencil.evolus.vn/Next.html) - GUI Prototyping Tool
- apt [Gimp](https://www.gimp.org/) - The Free & Open Source Image Editor
- apt [Blender](https://www.blender.org/) - Open Source 3D creation. Free to use for any purpose, forever.
- apt [Synfig](http://www.synfig.org/) - Open-source 2D animation software
- apt [Darktable](http://www.darktable.org/) - an open source photography workflow application and raw developer

#### 6. Student
- apt [Code::Block](http://www.codeblocks.org/) - C, C++ and Fortran IDE built to meet the most demanding needs of its users.
- apt [NetBeans](http://netbeans.org/)
- apt gcc & g++ Compiler
- [OpenCV](http://opencv.org) - a library of programming functions mainly aimed at real-time computer vision.
- [Git](https://git-scm.com/) - for Versioning Control

Masih terasa hambar? Tambahkan versimu di [sini](https://github.com/tealinuxos/modularitea/issues/new)

# Kontribusi
Status proyek modularitea saat ini masih dalam pengembangan, kamu dapat berkontribusi apapun. Baik itu ide, dokumentasi, desain ataupun kode. [Buat issue untuk memulai kontribusi](https://github.com/tealinuxos/modularitea/issues/new) .

# Lainnya

Masih bingung ingin belajar atau menggunakan bahasa pemprograman apa ?

- [Best Programming Language to Learn](http://www.bestprogramminglanguagefor.me)
- [Which Programming Language Should I Learn?](http://choosing-a-language.techboss.co/)

# Lisensi
[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2016 TeaLinuxOS
