#!/usr/bin/env python

import os
import os.path

isoName = '/Users/mnain/Downloads/CentOS-7-x86_64-DVD-1503-01.iso'

print isoName
siz = os.stat(isoName).st_size
oneGB = 1024 * 1024 * 1024
units = siz / oneGB
basename = os.path.basename(isoName)
ss = os.path.splitext(basename)
print 'Exists:',os.path.exists(isoName)
print 'Size:',siz
print siz / oneGB
print ss
fin = open(isoName, 'rb')
extNum = 1
totalSiz = 0
for i in range(units):
	foutName = "%s.%03d" % (ss[0],i)
	#print ss[0],extNum
	extNum = extNum + 1
	print foutName
	fout = open(foutName, 'wb')
	oneBuf = fin.read(oneGB)
	fout.write(oneBuf)
	fout.close()
	totalSiz = totalSiz + oneGB
	extNum = i
if totalSiz < siz:
	extNum = extNum + 1
	print "Extnum=", extNum
	foutName = "%s.%03d" % (ss[0],extNum)
	print foutName
	print "need to copy ",siz-totalSiz
	diffToCopy = siz-totalSiz
	oneBuf = fin.read(diffToCopy)
	fout = open(foutName, 'wb')
	fout.write(oneBuf)
	fout.close()
fin.close()


