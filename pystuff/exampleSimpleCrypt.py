#!/usr/bin/env python

import SimpleCrypt
import base64
import getpass
import MyKey

if __name__ == "__main__":
	key = 'MyOriginal20!6Key'
	key = MyKey.MyKey().read()
	print('key='+key)
	sc = SimpleCrypt.SimpleCrypt(key)
	#print(dir(sc))
	orig = "SecretString123!$"
	#orig = raw_input('Password:')
	orig = getpass.getpass()
	enc = sc.Encrypt(orig)
	encoded = base64.b64encode(enc)
	print(encoded)
	v = sc.Decrypt(enc)
	print(v)

