#!/usr/bin/env python

import sys
import os
import subprocess
import getpass
import Crypto.Cipher.AES
import random
import base64
import paramiko
import getopt
import socket
import colors

_VERSION = "0.1a May 23, 2014"
_SALT = "MyS3r!!tAng@l"
_BLOCKSIZE = 32
_PADDING = ' '
_HOST = 'host'
_USER = 'user'
_CMD = 'cmd'
_PASSWORDS = { 'ncoadmin' : 'n3tc00l', 'emadmin' : 'Tempr00t!!long', 'oracle' : 'oracle', 'db2inst1' : 'n3tc00l' }

def check_one(host, cmd):
	print "Host",host,"Cmd",cmd

def genSalt(length):
	array = []
	for i in range(length):
		r = random.randrange(33,126)
		array.append(r)
	#print array
	chArray = ""
	for i in range(length):
		chArray += chr(array.pop())
	#print chArray
	return chArray
	
def pad(s):
	return s + (_BLOCKSIZE - len(s) % _BLOCKSIZE) * _PADDING

def unused():
	cleartext = getpass.getpass()
	cleartext = pad(cleartext)
	print cleartext
	#print crypt.crypt(cleartext, _SALT)
	iv = genSalt(16)
	#key = Crypto.Random.new().read(Crypto.Cipher.AES.block_size)
	key = genSalt(16)
	aes = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_ECB, iv)
	#encoded = base64.b64encode(aes.encrypt(cleartext))
	print cleartext, iv, key
	encoded = base64.b64encode(aes.encrypt(cleartext))
	print "Enc:",encoded
	decoded = aes.decrypt(base64.b64decode(encoded))
	print "Dec:",decoded
	
def showOut(array):
	redList = ['unrecognized service', 'dead', 'DEAD', 'PENDING', 'process not running', 
				"Not Ok", "Not OK", "Stopped", "stopped", "FAILED", "Failed", "WAIT_HB", "not working",
				"WAITING", "not running", "NOT running", "NOT RUNNING", "cannot be reached" ]
	greenList = ['running', 'RUNNING', 'Running', 'Started', 'OK', 'Ok', 'STARTED']
	#redList = []
	#greenList = []
	for l in array:
		redFound = False
		for r in redList:
			if l.find(r) != -1:
				redFound = True
				l = l.replace(r, colors.rred()+r+colors.off())
		if redFound == False:
			for g in greenList:
				if l.find(g) != -1:
					l = l.replace(g, colors.green()+g+colors.off())
		l = l.rstrip()
		print "OUT:",l

if __name__ == "__main__":
	print "Version:",_VERSION
	_DEFAULT_PROC_LIST = 'proclist.txt'
	procListFile = _DEFAULT_PROC_LIST
	(opts,args) = getopt.getopt(sys.argv[1:], "p:")
	for o in opts:
		if o[0] == "-p":
			procListFile = o[1]
	procList = open(procListFile, 'r').readlines()
	procList = map((lambda x: x.rstrip()), procList)
	allHosts = []
	oneHost = {}
	for p in procList:
		if not p.startswith('#'):
			array = p.split('^')
			oneHost[_HOST] = array[0]
			oneHost[_USER] = array[1]
			oneHost[_CMD] = array[2]
			#print oneHost #, _PASSWORDS[oneHost[_USER]]
			print "="*15,oneHost[_HOST],"="*15
			ssh = paramiko.SSHClient()
			try:
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				ssh.connect(oneHost[_HOST], username=oneHost[_USER], password=_PASSWORDS[oneHost[_USER]])
				(cin,cout,cerr) = ssh.exec_command(oneHost[_CMD])
				outLines = cout.readlines()
				errLines = cerr.readlines()
				if len(outLines) == 0 and len(errLines) == 0:
					print colors.rred() + "No process found" + colors.off()
					#print "No errors found"
				else:
					showOut(outLines)
					showOut(errLines)
			except paramiko.ssh_exception.SSHException:
				print colors.rred()+"Unable to connect"+colors.off()
				#print "Unable to connect"
			except socket.error:
				print colors.red()+"Unable to connect, socket error"+colors.off()
				#print "Unable to connect, socket error"
			except:
				pass
			finally:
				ssh.close()
