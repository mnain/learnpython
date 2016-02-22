#!/usr/bin/env python

import os
import sys
import urllib2
import colors

def doGet(u):
	try:
		resp = urllib2.urlopen(url=u, timeout=20)
		print u,colors.green()+'Ok'+colors.off(),resp.code
	except:
		print u,colors.red()+str(sys.exc_info()[1])+colors.off()
	

if __name__ == "__main__":
	tipUrls = ['http://tip.goes:16310/ibm/console',
				'http://tip-pri.goes:16310/ibm/console',
				'http://tip-sec.goes:16310/ibm/console',
				'http://teps-pri.goes:1920',
				'http://teps-sec.goes:1920',
				'http://impact-pri.goes:9080/nci',
				'http://impact-sec.goes:9080/nci',
				]
	for u in tipUrls:
		doGet(u)
