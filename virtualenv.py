#!/usr/bin/env python
from subprocess import call
import sys
#os.system("sudo apt-get install -y python-virtualenv")
call(["virtalenv", str(sys.argv[1:])])
