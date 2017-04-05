#! /usr/bin/python3

import sys
import json
import os
import subprocess
import apt
import apt_pkg
import apt.progress.text
import apt.progress.base
from urllib.request import urlretrieve
from gi.repository import Gtk

# harus diganti saat rilis
PREFIX = '/home/mnirfan/Projects/modularitea/'

# executable apt
APT_PATH = "/usr/bin/apt"


apt_available = os.path.isfile(APT_PATH)

# tambahkan direktori user ke aplikasi agar bisa import
sys.path.insert(PREFIX, 0)

class Atom:
    name = ''
    data = ''

    def __init__(self, atom_name):
        self.name = atom_name
        with open(PREFIX + 'atoms/'+self.name+'/package.json') as json_file:
            self.data = json.load(json_file)

    def install(self):
        # print(self.data)
        prefered_source = self.data['package']['prefered_source']
        print("prefered source: ", self.data['package']['prefered_source'])
        if prefered_source == "ubuntu-apt" and apt_available:
            self.install_with_apt()
        elif prefered_source == "http_download":
            self.install_from_download()

    def install_from_download(self, progress):
        # http://stackoverflow.com/questions/13881092/download-progressbar-for-python-3#13895723
        def reporthook(blocknum, blocksize, totalsize):
            readsofar = blocknum * blocksize
            progress.set_fraction(readsofar)



    def install_with_apt(self):
        print("install with apt...")
        if 'ppa' in self.data['package']['source']['ubuntu-apt']:
            print("adding ppa...")
            p = subprocess.Popen(['apt-add-repository', '--yes', self.data['package']['source']['ubuntu-apt']['ppa']],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            response = p.communicate()
            if p.returncode == 0:
                print("ppa added")
                c = apt.Cache()
                c.update()
                c[self.get_package_name()].mark_install()
                c.commit(fetch_progress=apt.progress.text.AcquireProgress)
        else:
            c = apt.Cache()
            c[self.get_package_name()].mark_install()
            c.commit()

    def get_package_name(self):
        return self.data['package']['source']['ubuntu-apt']['name']
