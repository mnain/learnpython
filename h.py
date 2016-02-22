
#!/usr/bin/env python

import sys

if len(sys.argv[1:]) == 0:
 print "Need environment eg. wst | wso | rso ..."
 sys.exit(1)

env = sys.argv[1]
ext = ".ssd.goes"
hostList = [1,3,4,5,6,7,8,10,11,12,13,14,16,19,20,22,24,26,27]
if env.startswith("nn"):
 hostList = [4,11,27]
 ext = ".nsd.goes"


for i in hostList:
  host = env + "-emvirt" + ("%03d" % i) + "a" + ext
  print host
  if env.startswith("nn"):
    host = env + "-emvirt" + ("%03d" % i) + "b" + ext
    print host
