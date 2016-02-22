#!/usr/bin/env python

import sys
import getpass
import zlib
import getopt

def encrypt():
	passwd = getpass.getpass()
	compressed = zlib.compress(passwd)
	fh = open('.secret', 'wb')
	fh.write(compressed)
	fh.close()

def decrypt():
	pass

if __name__ == "__main__":
	print dir(getopt)
	print getopt.__doc__
