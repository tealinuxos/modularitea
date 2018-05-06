import os
import sys
import json

# http://stackoverflow.com/questions/5721529/running-python-script-as-root-with-sudo-what-is-the-username-of-the-effectiv
user = os.getenv("SUDO_USER")

#USER_ATOMS_DIR = '/home/' + user + '/.modulaitea/atoms/'
SYS_ATOMS_DIR = '/usr/share/modularitea/atoms/'



class Atom:
    # atribut objek Atom
    object = None
    preferred_source = None
    _atom = None

    # inisialisasi objek
    # package: string | nama paket atom (nama folder)
    # return: None
    def __init__(self, package):
        self._atom = package
        # parsing JSON ke objek
        if os.path.exists(USER_ATOMS_DIR + package):
            with open(USER_ATOMS_DIR + package + '/package.json') as data:
                self.object = json.load(data)
        elif os.path.exists(SYS_ATOMS_DIR + package + '/package.json'):
            with open(SYS_ATOMS_DIR + package + '/package.json') as data:
                self.object = json.load(data)
        else:
            print("Atom \"" + package + "\" doesn't exist")
            exit(1)

        # default sumber pemasangan atom
        self.preferred_source = self.object['package']['preferred_source']

    def get_preferred_source(self):
        return self.object['package']['preferred_source']

    def get_name(self):
        return self.object['package']['name']

    def get_apt_package_name(self):
        if "ubuntu_apt" in self.object['package']['source']:
            return self.object['package']['source']['ubuntu_apt']['name']
        else:
            return None

    def get_ppa(self):
        if "ubuntu_apt" in self.object['package']['source']:
            if "ppa" in self.object['package']['source']['ubuntu_apt']:
                return self.object['package']['source']['ubuntu_apt']['ppa']
        else:
            return None

    def get_url(self, architecture="any"):
        source = self.object['package']['source']
        # print(source, architecture)
        if "http_archive" in source:
            if architecture == 32 and "32bit" in source['http_archive']:
                return source['http_archive']['32bit']['url']
            elif architecture == 64 and "64bit" in source['http_archive']:
                return source['http_archive']['64bit']['url']
            else:
                return source['http_archive']['any']['url']

    def get_archive_install_dir(self, architecture="any"):
        source = self.object['package']['source']
        if "http_archive" in source:
            if architecture == 32 and "32bit" in source['http_archive']:
                return source['http_archive']['32bit']['destination']
            elif architecture == 64 and "64bit" in source['http_archive']:
                return source['http_archive']['64bit']['destination']
            else:
                return source['http_archive']['any']['destination']

    def get_custom_desktop_entry(self):
        if os.path.isfile(USER_ATOMS_DIR + self._atom + "/" + self._atom + ".desktop"):
            return USER_ATOMS_DIR + self._atom + "/" + self._atom + ".desktop"
        elif os.path.isfile(SYS_ATOMS_DIR + self._atom + "/" + self._atom + ".desktop"):
            return SYS_ATOMS_DIR + self._atom + "/" + self._atom + ".desktop"
        else:
            return None
