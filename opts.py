#!/usr/bin/env python

import os
import sys
import optparse

NOCOLOR=None
PATH=None

def handleArgs(args):
	parser = optparse.OptionParser()
	parser.add_option('-n', '--nocolor', action='store_true', default=False, help='Set nocolor mode i.e. no highlighting', metavar=NOCOLOR)
	parser.add_option('-p', '--path', dest='path', help='Set the path of the config file', metavar=PATH)

	#print dir(parser)
	#print optparse.__doc__
	(opts,argList) = (None,None)
	(opts,argList) = parser.parse_args(args)
	print "opts:",opts
	print "argList:",argList


if __name__ == "__main__":
	handleArgs(sys.argv[1:])
