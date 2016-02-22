#!/usr/bin/env python

import sys
import os
import subprocess
import optparse
import  ConfigParser

def getConfirmation(cmdType):
    if cmdType == '1':
        print "="*60
	print "WARNING WARNING WARNING WARNING WARNING WARNING WARNING"
        print "="*60
	print "Are you Sure you want to SHUTDOWN ALL Servers ? yes/no"
        print "   "
    else:
       print "="*60
       print "WARNING WARNING WARNING WARNING WARNING WARNING WARNING"
       print "="*60
       print "Are you Sure you want to STARTUP ALL Servers ? yes/no"
       print "   "
    a = raw_input('Enter:')
    return a

def getCommandType():
    print "Enter '1' to shutdown all hosts"
    print "Enter '2' to power on all hosts"
    cmdtype = raw_input('Enter:')
    return cmdtype

def sendCommand(cmdType,immHostFile,userid,passwd):
	TMP_PATH = '/tmp/'
	if os.path.exists(immHostFile):
		allHosts = open(immHostFile, 'rt').readlines()
		#####sp = getServerPrefix(site,site_env)
		###print sp
		for aHost in allHosts:
			aHost = aHost.strip('\n')
			outName = TMP_PATH+aHost + ".log"
			errName = TMP_PATH+aHost + ".err"
			if cmdType == '1':
				cmd = "sudo ipmitool -I lan -H " + aHost + " -U " + userid + " -P " + passwd + " chassis power soft"
			elif cmdType == '2':
				cmd = "sudo ipmitool -I lan -H " + aHost + " -U " + userid + " -P " + passwd + " chassis power on"
			print cmd
			try:
				outFile = file(outName, 'wt')
        			errFile = file(errName, 'wt')
        			p = subprocess.Popen(cmd, shell=True, bufsize=16000, executable=None, stdin=None, stdout=outFile, stderr=errFile).wait()
        			outFile.close()
        			errFile.close()
			except OSError:
        				print sys.exc_info()
	else:
		print "hosts.txt file does not exists"


if len(sys.argv[1:]) <=1:
	print "Usage*: python ipmitool_cmd -c <<config-File>>"
	print "For example:  python ipmitool_cmd -c ipmi-rbu.cfg"
	sys.exit(1)
else:
	parser = optparse.OptionParser()

	parser.add_option("-c", "--config", dest="config", help="configuration file", metavar="CONFIG")

        (options, args) = parser.parse_args()
	#print "options=",options
        #print "args=",args
        print "config="+str(options.config)
        print "="*20
	if os.path.exists(options.config):
                print "config file : " +options.config
                cp = ConfigParser.ConfigParser()
                allConfigValues = cp.read(options.config)
                userid = cp.get('cfg', 'loginid')
                passwd = cp.get('cfg', 'password')
                site = cp.get('cfg', 'site')
                immHostFile = cp.get('cfg', 'immhostfilepath')
		cmdType = getCommandType()
		if getConfirmation(cmdType) == 'yes':
			sendCommand(cmdType,immHostFile,userid,passwd)
		
	else:
		print "failed on options file"

