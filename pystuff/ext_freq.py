#!/usr/bin/env python

import glob
import sys
import os

if __name__ == "__main__":
	pathName = "/Users/madannain/Downloads/*"
	allFiles = glob.glob(pathName)
	#print allFiles
	freqDict = {}
	for f in allFiles:
		#print "D = "+f,'|'
		elem = os.path.split(f)
		ext=os.path.splitext(elem[-1])[-1]
		if freqDict.has_key(ext):
			freqDict[ext] = freqDict[ext] + 1
		else:
			freqDict[ext] = 1
	print freqDict
