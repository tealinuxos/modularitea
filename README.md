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
- [Apache2](https://httpd.apache.org/) - Webserver
- [PHP 7](http://php.net) - a server scripting language
- [Composer](https://getcomposer.org/) -  Dependency Manager for PHP
- [MySql](https://www.mysql.com/) - a database system used on the web
- [PHPMyAdmin](https://www.phpmyadmin.net/) - Bringing MySQL to the web
- [Atom](https://atom.io/) - A hackable text editor
- [Git](https://git-scm.com/) - for Versioning Control
- [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/) - Built for those who build the Web

#### 2. Front-end Web Developer (FeWD)
Tipe pengembang ini akan berhubungan dengan antarmuka tampilan web.
- [NodeJS](https://nodejs.org) -  is an open-source, cross-platform JavaScript runtime environment for developing a diverse variety of tools and applications
- [Npm](https://www.npmjs.com/) - npm is the package manager for JavaScript
- [Bower](https://bower.io/) - A package manager for the web
- [Git](https://git-scm.com/) - for Versioning Control
- [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/) - Built for those who build the Web

#### 3. Back-end Web Developer (BeWD)
Tipe pengembang ini akan berhubungan dengan server dan database web.
- [Apache2](https://httpd.apache.org/) - Webserver
- [PHP 7](http://php.net) - a server scripting language
- [Composer](https://getcomposer.org/) -  Dependency Manager for PHP
- [MySql](https://www.mysql.com/) - a database system used on the web
- [PHPMyAdmin](https://www.phpmyadmin.net/) - Bringing MySQL to the web
- [Git](https://git-scm.com/) - for Versioning Control
- [MongoDB](https://www.mongodb.com/) - an open-source document database and leading NoSQL database
- [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/) - Built for those who build the Web
- [NodeJS](https://nodejs.org) -  is an open-source, cross-platform JavaScript runtime environment for developing a diverse variety of tools and applications
- [Npm](https://www.npmjs.com/) - npm is the package manager for JavaScript

#### 4. Mobile Android Developer (MAD)
Tipe pengembang ini akan berhubungan dengan pengembangan aplikasi mobile Android.
- [Android Studio](https://developer.android.com/studio/index.html) - The Official IDE for Android
- [SQLite Database Browser](http://sqlitebrowser.org/) - The Official home of the DB Browser for SQLite
- [Git](https://git-scm.com/) - for Versioning Control

#### 5. User Interface Designer (UID)
Tipe pengembang ini akan berhubungan dengan desain antarmuka, baik web, mobile maupun destop.
- [Inkscape](https://inkscape.org/) - for designing User Interface
- [Pencil](http://pencil.evolus.vn/Next.html) - GUI Prototyping Tool
- [Gimp](https://www.gimp.org/) - The Free & Open Source Image Editor
- [Blender](https://www.blender.org/) - Open Source 3D creation. Free to use for any purpose, forever.
- [Synfig](http://www.synfig.org/) - Open-source 2D animation software
- [Darktable](http://www.darktable.org/) - an open source photography workflow application and raw developer

#### 6. Student
- [Code::Block](http://www.codeblocks.org/) - C, C++ and Fortran IDE built to meet the most demanding needs of its users.
- [NetBeans](http://netbeans.org/)
- gcc & g++ Compiler
- [OpenCV](http://opencv.org) - a library of programming functions mainly aimed at real-time computer vision.
- [Git](https://git-scm.com/) - for Versioning Control

#### 7. Electronics Engineer (EE)
- [Eagle](http://www.cadsoft.de/) - A printed circuit board design tool.
- [gEDA](http://www.geda-project.org/) - GPL suite of Electronic Design Automation tools.
- [Icarus Verilog](http://icarus.com/eda/verilog/) - Icarus Verilog is a Verilog simulation and synthesis tool. It operates as a compiler, compiling source code written in Verilog (IEEE-1364) into some target format.
- [KiCad](http://kicad-pcb.org/) - is a portable, cross-platform, Free/Libre/Open-Source EDA Suite that is capable of schematic and printed circuit board design.
- [oregano](https://github.com/drahnr/oregano) - Schematic capture, netlists, and spice for simulations.
- [Qucs](http://qucs.sourceforge.net/index.html) - An integrated circuit simulator.
- [Fritzing](http://fritzing.org/) - electronic design automation software.

### 8. CAD Engineer (CadE)
- [BRL-CAD](http://www.brlcad.org/) - A Open Source 3D-CAD program. It is a Constructive Solid Geometry (CSG) solid modeling system with over 20 years development and production use by the U.S. military.
- [FreeCAD](http://www.freecadweb.org/) - Modern Open Source parametric CAD modeler geared toward mechanical engineering, product design and architecture among others, fully expandable through Python.
- [gCAD3D](http://www.gcad3d.org/) - A 3D-surface-CAD/CAM. Program is freeware.
- [LibreCAD](http://librecad.org/cms/home.html) - A 2D CAD application. Highly active fork of QCad, ported to Qt4.
- [MEDUSA](http://www.cad-schroer.com/products/medusa4-personal.html) - 2D/3D commercial mechanical engineering CAD. Free for personal use only.
- [Varkon](http://varkon.sourceforge.net/) - Open Source 3D- (parametric) and 2D-Development platform for a CAD program.

### 9. Mathematical Analysis Engineer (MaTE)
- [Octave](http://www.gnu.org/software/octave/) - GNU Octave is a FOSS high-level interpreted language, primarily intended for numerical computations of linear and nonlinear problems.
- [Sage](http://www.sagemath.org/) - A free open-source mathematics software system licensed under the GPL.
- [Scilab](http://www.scilab.org/) - An open source, cross-platform numerical computational package and a high-level, numerically oriented programming language. It can be used for signal processing, statistical analysis, image enhancement, fluid dynamics simulations, numerical optimization, and modeling, simulation of explicit and implicit dynamical systems and (if the corresponding toolbox is installed) symbolic manipulations.

### 10. Finite Element Analysis Engineer (FEAE)
- [Elmer](http://www.csc.fi/english/pages/elmer) - Elmer is an open source computational tool for multi-physics problems. It has been developed by CSC in collaboration with Finnish universities, research laboratories and industry.
- [Gmsh](http://www.geuz.org/gmsh/) - An automatic 3D finite element grid generator with a built-in CAD engine and FEM post-processor.
- [Netgen](https://ngsolve.org/) - Netgen is a multi-platform automatic mesh generation tool written in C++ capable of generating meshes in two and three dimensions. Netgen has FEM-ngolve CFD-ngflow extensions.
- [OOFem](http://www.oofem.org/) - A free finite element code with object oriented architecture for solving mechanical, transport and fluid mechanics problems.
- [Salome](http://www.code-aster.org/V2/spip.php?article303) - A Open Source software suite including Pre-/Post processing Tools: 3D-CAD, Mesher, FEM-Software

### 11. Fluid Mechanic Engineer (FME)
- [GHydraulics](http://epanet.de/ghydraulics/) - It's a Quantum GIS plugin that allows to export water supply networks for analysis in EPANET.
- [OpenFOAM](http://www.openfoam.com/) - A free, open source CFD software package to solve anything from complex fluid flows involving chemical reactions, turbulence and heat transfer, to solid dynamics and electromagnetics.
- [SU2](http://su2.stanford.edu/) - A free and open source suite of tools for analysis and shape design using gradient-based optimization.
- [XFoil](http://ubuntuforums.org/showthread.php?t=288920) - A program to design and/or calculate airfoils.

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
