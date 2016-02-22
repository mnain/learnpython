#!/usr/bin/env python

import sys

if len(sys.argv[1:]) == 0:
    print "Need environment eg. wst | wso | rso ..."
    sys.exit(1)

env = sys.argv[1]
ext = ".ssd.goes"
if ext.startswith("n"):
    ext = ".nsd.goes"

for i in range(1,28):
    host = env + "-emvirt" + ("%03d" % i) + "a" + ext
    print host
    if i >= 15 and i <= 18:
        host = env + "-emvirt" + ("%03d" % i) + "b" + ext
