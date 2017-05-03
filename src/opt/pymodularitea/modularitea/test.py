#! /usr/bin/python3

from resumable import urlretrieve
from apt_pkg import size_to_str

def reporthook(bytes_so_far, chunk_size, total_size):
    print(size_to_str(bytes_so_far * chunk_size), "of", size_to_str(total_size))

url = "http://pinguin.dinus.ac.id/iso/archlinux/archlinux-2017.03.01-dual.iso"
urlretrieve(url,
            "arch.iso",
            reporthook)