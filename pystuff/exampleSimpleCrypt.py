#!/usr/bin/env python

import SimpleCrypt
import base64

if __name__ == "__main__":
	sc = SimpleCrypt.SimpleCrypt('MyOriginal20!6Key')
	print(dir(sc))
	orig = "SecretString123!$"
	orig = raw_input('Password:')
	enc = sc.Encrypt(orig)
	encoded = base64.b64encode(enc)
	print(encoded)
	v = sc.Decrypt(enc)
	print(v)

