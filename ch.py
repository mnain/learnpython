#!/usr/bin/env python
#
# multi_threaded check_process
# for multiple hosts - read the file, assuming one host per line
#

import sys
import os
import subprocess
import getopt
import threadpool

def doPing(h):
 ping_response = subprocess.Popen(["/bin/ping", "-c1", "-W3", h ], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
 rc = " Ok"
 if ping_response.find('1 received') == -1:
  rc = " Fail"
 #print ping_response.rstrip(), h+rc
 #print h+rc
 return h+rc
 #return ping_response.find('1 received') != -1

def red():
 return chr(27)+"[91m"

def green():
 return chr(27)+"[92m"

def off():
 return chr(27)+"[0m"

def showResults(a,b):
 if b.find('Ok') != -1:
    print green()+b+off()
 else:
    print red()+b+off()

def showUsage():
	print "Usage:"

if __name__ == "__main__":
	# defaults
	colorMode = True
	moduleName = "proclist.txt"
	# check if arguments passed
	if len(sys.argv[1:]) > 0:
		try:
			(opts,args) = getopt.getopt(sys.argv[1:], "p:cq")
			if len(opts) > 0:
				print "Options:",opts
			if len(args) > 0:
				print "Arguments:",args
		except getopt.GetoptError,e:
			print e
