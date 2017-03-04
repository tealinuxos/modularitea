#! /usr/bin/python3

import sys
import json
import getpass
from .atom_ import Atom

# PREFIX = "/opt/"
PREFIX = "/home/mnirfan/Projects/"
sys.path.append(PREFIX+"modularitea/")

user = getpass.getuser()
USER_MODULE_DIR = '/home/' + user + '/.modulaitea/modules/'
SYS_MODULE_DIR = '/opt/modularitea/modules/'

def install_module(modules):
    pass
