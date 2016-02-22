#!/usr/bin/python

import os
import sys

if len(sys.argv[1:]) >= 1:
	#print "username:",sys.argv[1]
	username = sys.argv[1]
	if os.path.exists("/nethome/"+username) == True:
		print username,"nethome exists"
	else:
		print username,"nethome does not exist"
else:
	print "Need username"
