#!/usr/bin/env python

import sys
import glob

if len(sys.argv) == 1:
    print "*ERROR* : need arguments"
    sys.exit(1)
else:
    for f in sys.argv[1:]:
        allLines = open(f).readlines()
        for line in allLines:
            print f,line.rstrip()
        
