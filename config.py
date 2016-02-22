#!/usr/bin/env python

import sys
import os
import json
import getopt
from columns import *

config = { columns[LEVEL] : "authPriv",
            columns[AUTH_PROTOCOL] : "SHA",
            columns[AUTH_PASSPHRASE] : "secretWord",
            columns[PRIVACY_PROTOCOL] : "AES",
            columns[PRIVACY_PASSPHRASE] : "secretWord",
            columns[USERNAME] : "user",
            columns[HOSTNAME] : "dummyHost",
}

global engineIdConfig
engineIdConfig = "engineId.conf"

def writeConfig(conf):
    global engineIdConfig
    json.dump(conf, open(engineIdConfig, "wt"))

def readConfig():
    global engineIdConfig
    return json.load(open(engineIdConfig, "rt"))

def setConfigFile(fn):
    global engineIdConfig
    engineIdConfig = fn

def getConfigFile():
    global engineIdConfig
    return engineIdConfig

def usage():
    print sys.argv[0],"usage:"
    print "-r read configFile"
    print "-w write configFile"

if __name__ == "__main__":
    toWrite = toRead = False
    debugFlag = testFlag = False
    if len(sys.argv) == 1:
        usage()
        sys.exit(2)
    if len(sys.argv) > 1:
        (opts,args) = getopt.getopt(sys.argv[1:], "rwdt")
        for o in opts:
            if o[0] == '-r':
                toRead = True
            if o[0] == '-w':
                toWrite = True
            if o[0] == '-d':
                debugFlag = True
            if o[0] == '-t':
                testFlag = True
        if len(args) > 0:
            engineIdConfig = args[0]
        if debugFlag:
            print "engineIdConfig:",engineIdConfig
            print "toWrite:",toWrite
            print "toRead:",toRead
            sys.exit(1)
        if toWrite:
            writeConfig(config)
        if toRead:
            if os.path.exists(engineIdConfig):
                print readConfig()
            else:
                print engineIdConfig, "Does not exist or cannot access"
                sys.exit(10)
        print " "

