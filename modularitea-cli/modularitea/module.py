#! /usr/bin/python3

import os
import sys
import json
import subprocess

import shutil

from modularitea.atom import Atom
from modularitea.progress_adapter import printProgressBar
import platform
import time
import apt_pkg

RED = '\033[0;31m'
GREEN = '\033[0;32m'
CYAN = '\033[0;36m'
NOCOLOR = '\033[0m'
ACTION_INFO = "[" + CYAN + "*" + NOCOLOR + "]"
ACTION_SUCCESS = "[" + GREEN + "*" + NOCOLOR + "]"
ACTION_ERROR = "[" + RED + "*" + NOCOLOR + "]"

user = os.getenv("SUDO_USER")
home = "/home/"+user+"/"
USER_MODULE_DIR = '/home/' + user + '/.modulaitea/modules/'
SYS_MODULE_DIR = '/usr/share/modularitea-package/modules/'
print("SYS_MODULE_DIR", SYS_MODULE_DIR)

ARCH = 32
if platform.architecture()[0] == '64bit':
    ARCH = 64


class Module:
    module = None
    apt_atoms = []
    ppas = []
    http_atoms = []
    progressbar = None
    current_anim = 1

    def get_busy_anim(self):
        if self.current_anim == 1:
            self.current_anim += 1
            return "[\033[0;32m*\033[0m   ]"
        elif self.current_anim == 2:
            self.current_anim += 1
            return "[ \033[0;32m*\033[0m  ]"
        elif self.current_anim == 3:
            self.current_anim += 1
            return "[  \033[0;32m*\033[0m ]"
        elif self.current_anim == 4:
            self.current_anim = 1
            return "[   \033[0;32m*\033[0m]"

    def __init__(self, module_name):
        if os.path.exists(USER_MODULE_DIR + module_name):
            with open(USER_MODULE_DIR + module_name + '/package.json') as data:
                self.module = json.load(data)
            # print("module", module_name, "found in user dir")
        elif os.path.exists(SYS_MODULE_DIR + module_name):
            with open(SYS_MODULE_DIR + module_name + '/package.json') as data:
                self.module = json.load(data)
            # print("module", module_name, "found in sys dir")
        else:
            print(ACTION_ERROR, 'Module', module_name, "doesn't exist")
            exit(1)

        for atom in self.module['package']['atoms']:
            atom_temp = Atom(atom)
            # print("found ", atom_temp.get_name())
            # print(atom_temp.object['package']['preferred_source'])
            if atom_temp.object['package']['preferred_source'] == 'ubuntu_apt':
                self.apt_atoms.append(atom_temp)
                if "ppa" in atom_temp.object['package']['source']['ubuntu_apt']:
                    self.ppas.append(atom_temp.object['package']['source']['ubuntu_apt']['ppa'])
            elif atom_temp.object['package']['preferred_source'] == 'http_archive':
                self.http_atoms.append(atom_temp)
            else:
                print(ACTION_ERROR, "invalid atom", atom.get_name())
                exit(1)
                # raise AttributeError

        # print('APT      :', self.apt_atoms)
        # print('Download :', self.http_atoms)
        # print('PPA      :', self.ppas)

        if not os.path.exists(home + ".modularitea/download"):
            os.mkdir("{0}.modularitea".format(home))
            os.mkdir("{0}.modularitea/download".format(home))
        self.downloaded = 0
        # self.download_needed = self.get_download_size()

    def add_ppas(self):
        for ppa in self.ppas:
            print(ACTION_INFO, "menambahkan", ppa)
            p = subprocess.Popen(
                ['/usr/bin/apt-add-repository', '-y', ppa],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            # http://stackoverflow.com/questions/1606795/catching-stdout-in-realtime-from-subprocess
            for line in iter(p.stdout.read, b''):
                print(str(line, 'utf-8').rstrip(), end="")
        print(ACTION_INFO, "updating software list")
        p = subprocess.Popen(
            ["/usr/bin/apt", "update"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        for line in iter(p.stdout.readline, b''):
            print(str(line, 'utf-8').rstrip())

    def download_apt(self):
        apt_packages = []
        for package in self.apt_atoms:
            apt_packages.append(package.get_apt_package_name())
        print(ACTION_INFO, "downloading apt packages")
        p = subprocess.Popen(
            ["/usr/bin/apt", "download"] + apt_packages,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        for line in iter(p.stdout.readline, b''):
            print(str(line, 'utf-8').rstrip())


    def install_apt(self):
        apt_packages = ["apt","install", "-y", "--allow-unauthenticated"]
        for package in self.apt_atoms:
            apt_packages.append(package.get_apt_package_name())
        print(ACTION_INFO, "downloading apt packages")
        print(apt_packages)
        os.execv("/usr/bin/apt", apt_packages)
        # p = subprocess.Popen(
        #     ["/usr/bin/apt", "install", "-y"] + apt_packages,
        #     stderr=subprocess.PIPE,
        #     stdout=subprocess.PIPE
        # )
        # for line in iter(p.stdout.readline, b''):
        #     print(str(line, 'utf-8').rstrip())

    def download_archive(self):
        from urllib import request
        # for archive in self.http_atoms:
        #     self.time = time.time()
        #     file_location = home + ".modularitea/download/" + archive.get_url(ARCH).split('/')[-1]
        #     request.urlretrieve(
        #         archive.get_url(ARCH),
        #         file_location,
        #         self._report_hook
        #     )
        # print("download done")

        from resumable import urlretrieve, DownloadError
        import requests
        for archive in self.http_atoms:
            print(ACTION_INFO, "Downloading", archive.get_name())
            self.time = time.time()
            file_location = home + ".modularitea/download/" + archive.get_url(ARCH).split('/')[-1]
            print("   ", archive.get_url(ARCH))
            try:
                urlretrieve(
                    archive.get_url(ARCH),
                    # home + ".modularitea/download/" + archive.get_name().replace(" ", ""),
                    file_location,
                    self._report_hook
                )
            except DownloadError:
                print(ACTION_ERROR, "fail di download error")
                from urllib import request
                size = int(request.urlopen(archive.get_url(ARCH)).info()['Content-Length'])
                size_downloaded = os.path.getsize(file_location)
                if size_downloaded == size:
                    pass
                else:
                    raise DownloadError
            except requests.exceptions.ConnectionError as e:
                # todo: hapus debug
                # print("fail di ConnectionError")
                print(ACTION_ERROR, 'Error while downloading files. Check your internet connection')
                exit(1)
        print(ACTION_INFO, 'download done')
        return 0

    def _report_hook(self, bytes_so_far, chunk_size, total_size):
        downloaded = bytes_so_far * chunk_size
        prefix = "  " + apt_pkg.size_to_str(downloaded) + "B"
        printProgressBar(downloaded,
                         total_size,
                         prefix=prefix,
                         suffix=self.get_busy_anim())

    def install_archives(self):
        print(self.http_atoms)
        for atom in self.http_atoms:
            print("[*] memasang", atom.get_name())
            file_location = home + ".modularitea/download/" + atom.get_url(ARCH).split('/')[-1]
            command = []
            if file_location.endswith(".tar.gz") or file_location.endswith(".tar.xz"):
                command = ["/bin/tar", "-xvzf", file_location, "-C", atom.get_archive_install_dir(ARCH)]
            elif file_location.endswith(".zip"):
                command = ["/usr/bin/unzip", file_location, "-d", atom.get_archive_install_dir(ARCH)]
            p = subprocess.call(command)
            if atom.get_custom_desktop_entry():
                shutil.copyfile(
                    atom.get_custom_desktop_entry(),
                    # "/usr/share/applications"
                    "/tmp/" + atom._atom + ".desktop"
                )

    def get_download_size(self):
        from urllib import request
        total_size = 0
        for package in self.http_atoms:
            r = request.urlopen(package.get_url(ARCH))
            total_size += int(r.info()['Content-Length'])
            # print(package.get_name(),int(r.info()['Content-Length']))
        import apt
        c = apt.Cache()
        for package in self.apt_atoms:
            c[package.get_apt_package_name()].mark_install()
        total_size += c.required_download

        return total_size
