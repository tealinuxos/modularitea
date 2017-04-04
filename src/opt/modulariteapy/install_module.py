#! /usr/bin/python3

import os
import sys
import json
import getpass
from atom import Atom
from progress_adapter import CacheProgressAdapter, FetchProgressAdapter, InstallProgressAdapter
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess
import apt

# PREFIX = "/opt/"
PREFIX = "/home/mnirfan/Projects/"
sys.path.append(PREFIX+"modularitea/")

user = getpass.getuser()
# USER_MODULE_DIR = '/home/' + user + '/.modulaitea/modules/'
# SYS_MODULE_DIR = '/opt/modularitea/modules/'
USER_MODULE_DIR = PREFIX + 'modularitea/modules/'
SYS_MODULE_DIR = '/opt/modularitea/modules/'


class Module:
    module = None
    apt_atoms = None
    ppas = None
    http_atoms = None
    progressbar = None

    def __init__(self, module_name, progressbar:Gtk.ProgressBar, action_label):
        self.progressbar = progressbar
        self.action_label = action_label
        if os.path.exists(USER_MODULE_DIR + module_name):
            with open(USER_MODULE_DIR + module_name + '/package.json') as data:
                self.module = json.load(data)
        elif os.path.exists(SYS_MODULE_DIR + module_name):
            with open(SYS_MODULE_DIR + module_name + '/package.json') as data:
                self.module = json.load(data)
        else:
            print('Modul ' + module_name + " doesn't exist")
            # raise FileNotFoundError

        for atom in self.module['package']['atoms']:
            atom_temp = Atom(atom)
            if atom_temp.object['package']['preferred_source'] == 'ubuntu_apt':
                self.apt_atoms.append(atom_temp)
                if "ppa" in atom_temp.object['package']['source']['ubuntu_apt']:
                    self.ppas.append(atom_temp.object['package']['source']['ubuntu_apt']['ppa'])
            elif atom_temp.object['package']['preferred_source'] == 'http_download':
                self.http_atoms.append(atom_temp)
            else:
                raise AttributeError

        print('APT      :', self.apt_atoms)
        print('Download :', self.http_atoms)
        print('PPA      :', self.ppas)

    def add_ppas(self):
        for ppa in self.ppas:
            self.progressbar.set_text('adding ' + ppa)
            p = subprocess.Popen(
                ['apt-add-repository', '-y', ppa],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            response = p.communicate()
            if p.returncode == 0:
                print(ppa, "added")
            else:
                print(ppa, "failed")

    def install_apt(self, parent):
        fprogress = FetchProgressAdapter(
            self.progressbar,
            self.action_label,
            parent
        )
        c = apt.Cache()
        c.update(fetch_progress=fprogress)
        for package in self.apt_atoms:
            package.mark_install_apt()
        c.commit(fetch_progress=fprogress)

    def install_module(self, module_name, progressbar: Gtk.ProgressBar):
        pass

