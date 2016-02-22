#!/usr/bin/env python

import os
import sys
import getpass
import Crypto.Cipher.AES
import random
import base64
import hashlib

_VERSION = "0.1a May 27, 2014"
_SALT = "MyS3r!!tAng@l"
_BLOCKSIZE = 32
_PADDING = ' '

def genPass(clearText):
	r = random.randrange(1000,150000)
	aes = hashlib.sha256()
	aes.update(str(r))
	hd = aes.hexdigest()
	print r,len(hd),hd
	iv = hd[0:16]
	key = hd[32:]
	print iv,len(iv),key,len(key)
	aes = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_ECB, iv)
	encoded = aes.encrypt(clearText)
	e = iv+key+base64.b64encode(encoded)
	fh = open(".secret", 'w')
	fh.writelines(e)
	fh.close()

def checkOpenSSL():
	return True

if __name__ == "__main__":
	print sys.argv[0],_VERSION
	genPass('summer')
