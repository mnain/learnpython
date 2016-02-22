#!/usr/bin/env python
#
# multi_threaded ping
# to run for one host 'python pi.py hostname'
# to run for multiple hosts python pi.py @hostfile'
#
# for a single host we do not use threadpool
# for multiple hosts - read the file, assuming one host per line
#

import subprocess
import sys
import os
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

if __name__ == "__main__":
 if len(sys.argv) == 1:
  print "*ERROR*: Need ip/hostname to ping"

 if sys.argv[1].startswith('@'):
  #print "Expect a file"
  fname = sys.argv[1][1:]
  if os.path.exists(fname):
   allHosts = open(fname).readlines()
   tp = threadpool.ThreadPool(8)
   hostArray = []
   for h in allHosts:
    h = h.rstrip()
    hostArray.append(h)
   requests = threadpool.makeRequests(doPing, hostArray, showResults)
   for req in requests:
   	tp.putRequest(req)
   tp.wait()
 else:
  h = sys.argv[1]
  showResults(h, doPing(h))
