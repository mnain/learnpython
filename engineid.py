#!/usr/bin/python

# =============================================================================================
#
# engineid.py - build a list of machine ID's by reading hosts file
# takes the following arguments
# -c: CONFIG:      set configile (default: engineid.cfg)
# -l: LEVEL:       set security level (authPriv|noAuthNoPriv|authNoPriv), (default: authPriv)
# -a: PROTOCOL:    set authentication protocol (MD5|SHA), (default: SHA)
# -A: PASSPHRASE:  set authentication protocol passphrase
# -x: PROTOCOL:    set privacy protocol (AES|DES), (default: AES)
# -X: PASSPHRASE:  set privacy protocol passphrase
# -u: USERNAME:    set security username
# hostfile csv which has following columns:
#
# The command line arguments override values from config file.
# 
# =============================================================================================
# Edit History:
# Date          Person   Description
# ------------- -------- --------------------------
# Oct. 28, 2013 MN       Create
#
# =============================================================================================

# system libraries
import subprocess
import os
import sys
import csv
import getopt
import json
import subprocess
import time

# project libraries
from columns import *
from config import *

global cmdArgs
cmdArgs = "c:a:A:l:u:x:X:d"
global configFileName
configFileName = "engineid.cfg"
requiredOptions = ['-u', '-a', '-A', '-l', '-x', '-X']
global skipColumns
skipColumns = [ columns[HOSTNAME], columns[TYPE]]
global defaultCmd
defaultCmd = "snmpwalk -u {username} -l {level} -a {auth_protocol} -A {auth_passphrase} -x {privacy_protocol} -X {privacy_passphrase} {hostname} snmpEngineID.0"
global cmdFileName
cmdFileName = "cmd.txt"
global data
data = {}
global debugFlag
debugFlag = False
global SNMPKEY
SNMPKEY='snmpEngineId'

def usage():
    print sys.argv[0], "Usage:"
    print "-c: CONFIG:      set configile (default: "+configFileName+")"
    print "-l: LEVEL:       set security level (authPriv|noAuthNoPriv|authNoPriv), (default: authPriv)"
    print "-a: PROTOCOL:    set authentication protocol (MD5|SHA), (default: SHA)"
    print "-A: PASSPHRASE:  set authentication protocol passphrase"
    print "-x: PROTOCOL:    set privacy protocol (AES|DES), (default: AES)"
    print "-X: PASSPHRASE:  set privacy protocol passphrase"
    print "-u: USERNAME:    set security username"
    print "hostfile csv which has following columns:"
    indx = 0
    for c in columns:
        print "\t",indx,c
        indx = indx + 1

def oneHost(hostname, conf):
    global data
    #print "oneHost:"
    #print "hostname:",hostname
    #print "values:",conf
    outName = hostname + ".out"
    errName = hostname + ".err"
    cmdLines = open(cmdFileName, 'rt').readlines()
    if len(cmdLines) == 0:
        cmdFh = open(cmdFileName, 'wt')
        cmdFh.writelines(defaultCmd)
        cmdFh.close()
        cmdLines = open(cmdFileName, 'rt').readlines()
    cmd = cmdLines[0]
    if len(cmd) > 1:
        for col in columns:
            if col not in skipColumns:
                key = '{'+col+'}'
                cmd = cmd.replace('{'+col+'}', conf[col])
                #print key,col,conf[col]
        cmd = cmd.replace('{hostname}', hostname)
        #print cmd
        try:
            outFh = open(outName, 'wt')
            errFh = open(errName, 'wt')
            rc = subprocess.Popen(cmd, shell=True, bufsize=32000, executable=None, stdin=None, stdout=outFh, stderr=errFh).wait()
            if rc == 0:
                print hostname,"Ok"
                allOpLines = open(outName, 'rt').readlines()
                firstLine = allOpLines[0].rstrip().split("=")[1].split(':')[1].strip()
                k = firstLine.replace(' ', '')
                conf[SNMPKEY] = k
                data[hostname] = conf
            else:
                allErrLines = open(errName, 'rt').readlines()
                errMsg = hostname+" *ERROR* "
                for el in allErrLines:
                    if el.find('snmpget') != -1 or el.find('snmpwalk') != -1:
                        errMsg += el.rstrip()
                print errMsg
        except OSError:
            print host,sys.exc_info()
            outFh.close()
            errFh.close()
    outFh.close()
    errFh.close()


if __name__ == "__main__":
    data = {}
    (opts,args) = getopt.getopt(sys.argv[1:], cmdArgs)

    if len(args) == 0:
        usage()
        sys.exit(10)

    for o in opts:
        if o[0] == '-c':
            configFileName = o[1]
            if os.path.exists(configFileName):
                #print "new config:",configFileName
                #engineIdConfig = configFileName
                #print getConfigFile()
                setConfigFile(configFileName)
                #print getConfigFile()
                config = readConfig()
                #print "From file: ",config,configFileName
        if o[0] == '-u':
            config[columns[USERNAME]] = o[1]
            #print "user:", config[columns[USERNAME]]
        if o[0] == '-l':
            config[columns[LEVEL]] = o[1]
            #print "level:",config[columns[LEVEL]]
        if o[0] == '-a':
            config[columns[AUTH_PROTOCOL]] = o[1]
            #print "auth_protocol:",config[columns[AUTH_PROTOCOL]]
        if o[0] == '-A':
            config[columns[AUTH_PASSPHRASE]] = o[1]
            #print "auth_passphrase:",config[columns[AUTH_PASSPHRASE]]
        if o[0] == '-x':
            config[columns[PRIVACY_PROTOCOL]] = o[1]
            #print "privacy_protocol:",config[columns[PRIVACY_PROTOCOL]]
        if o[0] == '-X':
            config[columns[PRIVACY_PASSPHRASE]] = o[1]
            #print "privacy_passphrase:",config[columns[PRIVACY_PASSPHRASE]]
        if o[0] == '-d':
            debugFlag = True
    if debugFlag:
        print "hostfile(s)",args
        print "config:",config

    for fn in args:
        if os.path.exists(fn):
            allHosts = open(fn,'rt').readlines()
            allHosts = map((lambda x: x.rstrip()), allHosts)
            print allHosts
            for h in allHosts:
                oneHost(h, config)
    #print "Data:",data
    timeStamp = time.strftime("%Y%m%d%H%M%S")
    
    confFile = open('mttrap.conf.append'+'.'+timeStamp,'wt')
    excelCsv = open('SNMPV3_Config.csv'+'.'+timeStamp,'wt')
    excelCsv.writelines('Host,EngineID,Auth User,Auth Type,Auth Pass,Priv Type,Priv Pass,Device Type,Zone\n')
    
    for k in data.keys():
        row = data[k]
        if row.has_key(SNMPKEY):
            print k,row[SNMPKEY],row[columns[USERNAME]],row[columns[AUTH_PROTOCOL]],row[columns[AUTH_PASSPHRASE]],row[columns[PRIVACY_PROTOCOL]],row[columns[PRIVACY_PASSPHRASE]]
            #excelCsv.writelines(k+','+data[k][SNMPKEY]) #+','+authUser+','+authType+','+authPass+','+privType+','+privPass+',,\n')
            excelCsv.writelines(k+','+row[SNMPKEY]+','+row[columns[AUTH_PROTOCOL]]+','+row[columns[AUTH_PASSPHRASE]]+','+row[columns[PRIVACY_PROTOCOL]]+','+row[columns[PRIVACY_PASSPHRASE]]+'\n')
            #confFile.writelines('createUser -e 0x'+data[k][SNMPKEY]) #+' '+authUser+' '+authType+' '+authPass+' '+privType+' '+privPass+'\n')
            confFile.writelines('createUser -e 0x'+row[SNMPKEY]+' '+row[columns[USERNAME]]+' '+row[columns[AUTH_PROTOCOL]]+' '+row[columns[AUTH_PASSPHRASE]]+' '+row[columns[PRIVACY_PROTOCOL]]+' '+row[columns[PRIVACY_PASSPHRASE]]+'\n')
    confFile.close()
    excelCsv.close()
