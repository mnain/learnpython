#!/usr/bin/python

# =============================================================================================
#
# snmpget.py - build a list of machine ID's by reading hosts file
#
# =============================================================================================

import subprocess
import os
import sys

if len(sys.argv[1:]) == 0:
    print "*ERROR*: need hosts files"
    sys.exit(1)
hostFile = sys.argv[1]
if os.path.exists(hostFile) == False:
    print "*ERRO*: "+hostFile+" does not exist or has access problems"
    sys.exit(2)

print "="*5+" Processing "+hostFile+" "+"="*5

allHosts = open(hostFile, 'rt').readlines()
authUser = 'solaceTraps'
authType = 'MD5'
authPass = 'solaceTraps1'
privType = 'DES'
privPass = 'solaceTraps1'
cmd = 'snmpget -v3 -n "" -u '+authUser+' -a '+authType+' -A '+authPass+' -x '+privType+' -X '+privPass+' -l authPriv'
trailer = 'snmpEngineID.0'
outName = 'outfile.txt'
errName = 'err.txt'

origKeysFile = 'keys.txt'
origKeys = open(origKeysFile, 'rt').readlines()
keys = []
for k in origKeys:
    keys.append(k.rstrip())

data = {}
for h in allHosts:
    h = h.rstrip()
    fullCmd = cmd + ' ' + h + ' ' + trailer
    #print fullCmd
    try:
        outFile = file(outName, 'wt')
        errFile = file(errName, 'wt')
        rc = subprocess.Popen(fullCmd, shell=True, bufsize=16000, executable=None, stdin=None, stdout=outFile, stderr=errFile).wait()
        #print h,rc
        outFile.close()
        errFile.close()
        if rc == 0:
            #print fullCmd, rc
            allLines = open(outName, 'rt').readlines()
            firstLine = allLines[0].rstrip().split("=")[1].split(':')[1].strip()
            #print h+'|'+firstLine.replace(' ', '')
            k = firstLine.replace(' ', '')
            #if k in keys:
            #    print k,"found"
            data[h] = k
            os.remove(outName)
            os.remove(errName)
        else:
            errLines = open(errName, 'rt').readlines()
            print h,"*ERROR*"
            for l in errLines:
                print l
    except OSError:
        print sys.exc_info()
        outFile.close()
        errFile.close()

#print data

confFile = open('mttrap.conf.append','wt')
excelCsv = open('SNMPV3_Config.csv','wt')
excelCsv.writelines('Host,EngineID,Auth User,Auth Type,Auth Pass,Priv Type,Priv Pass,Device Type,Zone\n')
for k in data.keys():
    print k,data[k]
    excelCsv.writelines(k+','+data[k]+','+authUser+','+authType+','+authPass+','+privType+','+privPass+',,SOZ\n')
    confFile.writelines('createUser -e 0x'+data[k]+' '+authUser+' '+authType+' '+authPass+' '+privType+' '+privPass+'\n')
excelCsv.close()
confFile.close()
