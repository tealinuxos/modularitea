import os
import sys
import json
import getpass          # ambil username dari user aktif

# PREFIX = "/opt/"
PREFIX = "/home/mnirfan/Projects/"
sys.path.append(PREFIX+"modularitea/")

user = getpass.getuser()
# USER_ATOMS_DIR = '/home/' + user + '/.modulaitea/atoms/'
# SYS_ATOMS_DIR = '/opt/modularitea/atoms/'
USER_ATOMS_DIR = PREFIX + 'modularitea/atoms/'
SYS_ATOMS_DIR = '/opt/modularitea/atoms/'


class Atom:

    # atribut objek Atom
    object = None
    preferred_source = None

    # inisialisasi objek
    # package: string | nama paket atom (nama folder)
    # return: None
    def __init__(self, package):
        # parsing JSON ke objek
        if os.path.exists(USER_ATOMS_DIR + package):
            with open(USER_ATOMS_DIR + package + '/package.json') as data:
                self.object = json.load(data)
        elif os.path.exists(SYS_ATOMS_DIR + package + '/package.json'):
            with open(SYS_ATOMS_DIR + package + '/package.json') as data:
                self.object = json.load(data)
        else:
            print("Atom \"" + package + "\" doesn't exist")
            raise FileNotFoundError

        # default sumber pemasangan atom
        self.preferred_source = self.object['package']['preferred_source']

    # lakukan pemasangan otomatis
    # return: None
    def install(self):
        if self.preferred_source == "ubuntu_apt":
            self.mark_install_apt()
        elif self.preferred_source == "http_archive":
            self.install_http_archive()
        else:
            raise Exception

    # lakukan pemasangan dengan APT
    # return: None
    def mark_install_apt(self):
        if "ppa" in self.object['package']['source']['ubuntu_apt']:
            import subprocess
            process = subprocess.Popen(['apt-add-repository', '--yes', self.get_ppa()],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            process.communicate()
            if process.returncode == 0:
                print(self.get_ppa()+" added")
            else:
                raise Exception

        import apt
        cache = apt.Cache()
        cache[self.get_apt_name()].mark_install()

    # lakukan pemasangan dengan download dari website ekstensi .tar.gz dsb
    # return: None
    def install_http_archive(self):
        pass

    # lakukan pemasangan dengan download dari website ekstensi .deb
    # return: None
    def install_http_deb(self):
        pass

    # ambil nama paket APT jika tersedia
    # return: name(string) or None
    def get_apt_name(self):
        if "ubuntu_apt" in self.object['package']['source']:
            return self.object['package']['source']['ubuntu_apt']['name']
        else:
            return None

    def get_ppa(self):
        return self.object['package']['source']['ubuntu_apt']['ppa']