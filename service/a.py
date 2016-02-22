#!/usr/bin/env python

import sys
import os
import platform

#print dir(platform)
print ' '.join(platform.uname())
print "Python version:",platform.python_version()
print dir(platform)
print platform.python_compiler()
