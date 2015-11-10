#!/usr/bin/env python

from __future__ import print_function
import time
import sys

for i in range(100):
	time.sleep(1)
	print("%10d" % i, end='\r')
	sys.stdout.flush()
print("That's all folks!!!", end='\r')

