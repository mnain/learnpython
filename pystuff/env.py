import os
import sys
import platform

e = os.environ["PATH"].split(':')
for i in e:
	print i
print dir(platform)
print platform.uname()



