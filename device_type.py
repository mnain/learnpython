#!/usr/bin/env python

import sys
import os

if len(sys.argv) == 1:
    print "Need arguments"
    sys.exit(1)

for arg in sys.argv[1:]:
    print arg
