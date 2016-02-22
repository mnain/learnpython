#!/usr/bin/env python

import os
import sys
import paramiko
import getopt
import getpass

config = { 
	'user' : None, 
	'password' : None,
	'host' : None,
	'command' : None,
	'prompt' : False,
	}

def doCommand(conf):
	#print conf['command'],'on',conf['host'],'as',conf['user']
	#print conf['password']
	#print config
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(conf['host'], username=conf['user'], password=conf['password'])
	(cin,cout,cerr) = ssh.exec_command(conf['command'])
	try:
		#print "in",cin.readlines()
		outLines = cout.readlines()
		errLines = cerr.readlines()
		if len(outLines) > 0:
			for o in outLines:
				print o.rstrip()
		if len(errLines) > 0:
			for o in errLines:
				print o.rstrip()
	except:
		pass
	ssh.close()


if __name__ == "__main__":
	(opts,args) = getopt.getopt(sys.argv[1:], "h:u:c:p:A")

	#print "opts=",opts
	#print "args=",args


	if len(opts) > 0:
		#indx = 0
		for o in opts:
			#print indx,o[0]
			#indx = indx + 1
			if o[0] == '-u':
				config['user'] = o[1]
			if o[0] == '-c':
				config['command'] = o[1]
			if o[0] == '-p':
				config['password'] = o[1]
			if o[0] == '-h':
				config['host'] = o[1]
			if o[0] == '-A':
				config['prompt'] = True

	allHosts = []
	if len(args) > 0:
		indx = 0
		for a in args:
			print indx,a
			indx = indx + 1
			if os.path.exists(a):
				all = open(a, 'rt').readlines()
				for i in all:
					allHosts.append(i.rstrip())
				print allHosts

	if config['host'] == None:
		if len(allHosts) == 0:
			print "no hosts"
		else:
			if config['prompt'] == True:
				config['password'] = getpass.getpass()
			for h in allHosts:
				config['host'] = h
				doCommand(config)
	else:
		if config['prompt'] == True:
			config['password'] = getpass.getpass()
		doCommand(config)


