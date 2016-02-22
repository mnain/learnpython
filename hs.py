#!/usr/bin/python

import sys
import paramiko
import subprocess
import colors

_VERSION = "0.1a"

def doPing(h):
	ping_response = subprocess.Popen(["ping", "-c1", "-w3", h], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
	rc = colors.green()+" Ok"+colors.off()
	if ping_response.find('1 received') == -1:
		rc = colors.red()+" Fail"+colors.off()
	#print h+rc
	return h+rc

def doSsh(h):
	rc = 0
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(hostname=h, username='mnain')
		stdi,stdo,stde = ssh.exec_command('ls')
		data = stdo.readlines()
		rc = len(data)
		ssh.close()
	except:
		#print sys.exc_info()
		rc = 0
	if rc == 0:
		rValue = colors.red()+"  Fail "+colors.off()
	else:
		rValue = colors.green()+" Ok"+colors.off()
	return rValue

if __name__ == "__main__":
	print "Host Status",_VERSION
	allHosts = []
	try:
		allHosts = open(sys.argv[1], 'r').readlines()
		allHosts = map((lambda x: x.rstrip()), allHosts)
		#print allHosts
	except IOError:
		print "Unable to open sys.argv[1]"
		allHosts = []
	except IndexError:
		print "Illegal argument"
		allHosts = []
	finally:
		pass
	#print colors.green(),allHosts,colors.off()
	for h in allHosts:
		ping = doPing(h)
		ssh = doSsh(h)
		print ping,ssh
