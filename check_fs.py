#!/usr/bin/python

import os
import sys
import paramiko
import socket
import pi

fname = 'fileserverslist'
_PASSWORDS = [ 'emadmin' , 'Temproot!!long' ]

def nethomeExists(serv,user):
	print "Server:",serv
	ssh = paramiko.SSHClient()
	try:
		cmd = 'ls /nethome/'+user
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(serv, username='emadmin', password='Tempr00t!!long')
		(cin,cout,cerr) = ssh.exec_command(cmd)
		outLines = cout.readlines()
		errLines = cerr.readlines()
		if len(outLines) == 0 and len(errLines) == 0:
			print '/nethome/'+user+' does not exist'
		else:
			if len(outLines) > 2:
				print '/nethome/'+user+' exists'
			for e in errLines:
				print "ERR:",e
	except paramiko.ssh_exception.SSHException:
		print "Unable to connect"
	except socket.error:
		print "Unable to connect, socket error"
	except:
		pass
	finally:
		ssh.close()

if __name__ == "__main__":
	args = sys.argv[1:]
	if len(args) == 0:
		print "Need username"
		sys.exit(1)
	user = sys.argv[1]
	if os.path.exists(fname) == True:
		allServerList = open(fname, 'rt').readlines()
		for s in allServerList:
			if s.startswith('#') == False:
				server = s.rstrip()
				if pi.doPing(server.rstrip()).find("Ok") != -1:
					nethomeExists(server,user)
