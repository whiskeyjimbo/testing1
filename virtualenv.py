#!/usr/bin/env python
from subprocess import call
import os
import sys
os.system("sudo apt-get install -y python-virtualenv")
cmd = "virtualenv {0}".format(' '.join(sys.argv[1:]))
os.system(cmd)
