#!/usr/bin/env python

import sys
import random

rr = range(1,25)
#i = rr.index(9)
for i in rr:
	if i == 9:
		print "9 found"
		rr.pop()
print rr, i
#print dir(random)
random.shuffle(rr)
print rr

