#!/usr/bin/env python

import sys
import yaml
import beanstalkc

if __name__ == "__main__":
	print dir(beanstalkc)
	bs = beanstalkc.Connection(host='localhost', port=11300)
	print dir(bs)
	bs.close()
