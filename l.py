#!/usr/bin/python

import os
import sys
import subprocess

def nslookup(hostList):
	for h in hostList:
		outf = h + '.out'
		errf = h + '.err'
		try:
			outfh = open(outf, 'wt')
			errfh = open(errf, 'wt')
			cmd = 'nslookup ' + h
			rc = subprocess.Popen(cmd, shell=True, bufsize=64000, executable=None, stdin=None, stdout=outfh, stderr=errfh).wait()
			outfh.close()
			errfh.close()
			if rc == 0:
				allLines = open(outf, 'rt').readlines()
				print h,'--Ok--',allLines
			else:
				allLines = open(errf, 'rt').readlines()
				print h,'--Failed--',allLines
		except:
			''' handle subprocess error'''
			outfh.close()
			errfh.close()
			print h,sys.exc_info()

def readHostFile(hf):
	allHosts = []
	try:
		allHosts = open(hf,'rt').readlines()
		allHosts = map((lambda x: x.rstrip()), allHosts)
	except:
		print "Unable to read ",hf
	return allHosts

if __name__ == "__main__":
	ah = readHostFile(sys.argv[1])
	nslookup(ah)
