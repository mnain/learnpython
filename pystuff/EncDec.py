#!/usr/bin/env python

import sys
import os
import base64
import getpass
import MyKey
import SimpleCrypt

class EncDec:
	def __init__(self, key='10d25025b502987e3cbac85fe692e022bca150e13070bb4058c2038c06fe5add'):
		self.key = key
		self.sc = SimpleCrypt.SimpleCrypt(self.key)

	def __str__(self):
		return "<EncDec: key=%s>" % self.key


	def encrypt(self, msg):
		return base64.b64encode(self.sc.Encrypt(msg))

	def decrypt(self, encrypted):
		return self.sc.Decrypt(base64.b64decode(encrypted))

if __name__ == "__main__":
	ed = EncDec()
	secretFile = os.environ['HOME'] + os.sep + '.secret'
	if len(sys.argv) > 1:
		print(sys.argv[1:])
		if sys.argv[1] == '-d':
			fh = open(secretFile,'rt')
			line = fh.readline()
			fh.close
			print(line)
			print(ed.decrypt(line))
		if sys.argv[1] == '-e':
			passwd = getpass.getpass()
			encrypted = ed.encrypt(passwd)
			fh = open(secretFile, 'wt')
			fh.writelines(encrypted)
			fh.close()


