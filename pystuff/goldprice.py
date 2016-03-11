#!/usr/bin/python

import sys
import urllib2
import xml.etree.ElementTree 

URL = 'http://www.xmlcharts.com/'
#URL = 'http://www.nain.cc'

ht = urllib2.urlopen(URL)
body = ht.readlines()
allLines = ''
for line in body:
	allLines = allLines + line
print type(allLines)
print allLines
#tree = xml.etree.ElementTree.fromstring(allLines)
#print dir(tree)

