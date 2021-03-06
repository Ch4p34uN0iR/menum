#!/usr/bin/env python

from subprocess import call
import os
import sys
import datetime

if len(sys.argv) != 2:
   print(sys.argv[0] + " <targets-file>")
   sys.exit(1)

with open(sys.argv[1]) as f:
    hosts = [x.strip('\n') for x in f.readlines()]

for target in hosts:
    now = datetime.datetime.now()
    os.system("enum4linux -a " + target + " > " + now.strftime("%Y-%m-%d_%H:%M:%S") + "_enum4linux_" + target)
