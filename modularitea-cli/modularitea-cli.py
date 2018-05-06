#!/usr/bin/python3

import urllib

import time

from modularitea import module
from optparse import OptionParser
import apt_pkg

parser = OptionParser()
parser.add_option("-m", "--module", dest="module")

(option, args) = parser.parse_args()
if not option.module:
    parser.print_help()
    exit(-1)

try:
    module_name = option.module
    module_object = module.Module(module_name)

    print("memeriksa koneksi...")
    module_object.add_ppas()
    total_size = module_object.get_download_size()
    print("\n\n\033[0;36mDiperlukan unduhan sebesar", apt_pkg.size_to_str(total_size) + "B (perkiraan)")
    print("mulai mengunduh....")
    print("Tekan Ctrl + C untuk membatalkan (unduhan dapat diteruskan lain waktu)\033[0m")
    time.sleep(2)
    module_object.download_archive()
    module_object.install_archives()
    module_object.install_apt()
    exit(0)
except KeyboardInterrupt:
    print("\nkeyboard interrupt")
    exit(-3)
except urllib.error.URLError:
    print("\n[\033[0;31m*\033[0m] Tidak dapat mengunduh paket dari server. Periksa koneksi internetmu.")
    exit(-2)
