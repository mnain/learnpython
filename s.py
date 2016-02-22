#!/usr/bin/python

# =============================================================================================
#
# snmpwalk.py - build a list of machine ID's by reading hosts file
#
# =============================================================================================

import subprocess
import os
import sys
import csv
import columns

if len(sys.argv[1:]) == 0:
    print "*ERROR*: need hosts files"
    sys.exit(1)

hostFile = sys.argv[1]
if os.path.exists(hostFile) == False:
    print "*ERRO*: "+hostFile+" does not exist or has access problems"
    sys.exit(2)

print "="*5+" Processing "+hostFile+" "+"="*5
defaultCmdLine = "snmpget -u {username} -l {level} -a {protocol} -A {auth_passphrase} -x {privacy_protocol} -X {privacy_passphrase} {hostname} snmpEngineID.0"
cmdFile = 'cmd.txt'

if os.path.exists(cmdFile) == False:
    cmdFh = open(cmdFile, 'wt')
    cmdFh.writelines(defaultCmdLine)
    cmdFh.close()

cmd = open(cmdFile, 'r').readline()

data = {}
hostFh = open(hostFile, "rt")
csvDict = csv.DictReader(hostFh,columns.columns)
for h in csvDict:
    if h['username'] == 'username':
        continue
    for k in h.keys():
        if k != 'type':
            cmd = cmd.replace('{'+k+'}', h[k]) 
    #print cmd
    host = h['hostname']
    outFilename = host + '.out'
    errFilename = host + '.err'
    try:
        outFh = file(outFilename, 'wt')
        errFh = file(errFilename, 'wt')
        rc = subprocess.Popen(cmd, shell=True, bufsize=16000, executable=None, stdin=None, stdout=outFh, stderr=errFh).wait()
        #print host,rc
        outFh.close()
        errFh.close()
        if rc == 0:
            print host, "Ok"
            allLines = open(outFilename, 'rt').readlines()
            firstLine = allLines[0].rstrip().split("=")[1].split(':')[1].strip()
            #print host+'|'+firstLine.replace(' ', '')
            k = firstLine.replace(' ', '')
            h['snmpEngineId'] = k
            #print h
            data[host] = h
            #os.remove(outName)
            #os.remove(errName)
        else:
            errLines = open(errFilename, 'rt').readlines()
            errMsg = host+" *ERROR*"
            for l in errLines:
                if l.find('snmpget') != -1:
                    errMsg += " "+l.rstrip()
            print errMsg
    except OSError:
        print sys.exc_info()
        outFh.close()
        errFh.close()

print data
