#!/usr/bin/env python

import oscrypto.symmetric
import oscrypto.asymmetric
import oscrypto.util
import random
import pickle
import getpass
import base64
import os
import os.path

class PyEncDec:

    _KEY_FILENAME = ".key"
    _IV_FILENAME = ".iv"
    _SECRET_FILENAME = ".secret"

    def __init__(self):
        if not os.path.exists(self._KEY_FILENAME):
            self.key = oscrypto.util.rand_bytes(32)
            b64key = base64.b64encode(self.key)
            # print(b64key)
            # print(type(b64key))
            fhKey = open(self._KEY_FILENAME, 'wt')
            fhKey.write(b64key.decode('utf-8'))
            fhKey.close()
        else:
            oneline = open(self._KEY_FILENAME, 'rt').readlines()
            # print("Key : {}".format(oneline[0]))
            self.key = base64.b64decode(oneline[0])
        # print("Init Key : {}".format(self.key))
        if not os.path.exists(self._IV_FILENAME):
            self.iv = oscrypto.util.rand_bytes(16)
            b64iv = base64.b64encode(self.iv)
            fhIv = open(self._IV_FILENAME, 'wt')
            fhIv.write(b64iv.decode('utf-8'))
            fhIv.close()
        else:
            oneline = open(self._IV_FILENAME, 'rt').readlines()
            self.iv = base64.b64decode(oneline[0])
        # print("Init IV: {}".format(self.iv))
        
    def generateKey(self):
        if not os.path.exists(self._KEY_FILENAME):
            self.key = oscrypto.util.rand_bytes(32)
            b64key = base64.b64encode(self.key)
            # print(b64key)
            # print(type(b64key))
            fhKey = open(self._KEY_FILENAME, 'wt')
            fhKey.write(b64key.decode('utf-8'))
            fhKey.close()
        else:
            oneline = open(self._KEY_FILENAME, 'rt').readlines()
            # print("Key : {}".format(oneline[0]))
            self.key = base64.b64decode(oneline[0])
        # print("Init Key : {}".format(self.key))

    def generateIV(self):
        if not os.path.exists(self._IV_FILENAME):
            self.iv = oscrypto.util.rand_bytes(16)
            b64iv = base64.b64encode(self.iv)
            fhIv = open(self._IV_FILENAME, 'wt')
            fhIv.write(b64iv.decode('utf-8'))
            fhIv.close()
        else:
            oneline = open(self._IV_FILENAME, 'rt').readlines()
            self.iv = base64.b64decode(oneline[0])
        # print("Init IV: {}".format(self.iv))
    
    def show(self):
        outStr = "Key : {}, IV : {}".format(self.key, self.iv)
        return outStr
        
    def encrypt(self, secret):
        enc = oscrypto.symmetric.aes_cbc_pkcs7_encrypt(self.key, bytes(secret,'utf-8'), self.iv)
        print(enc)
        encoded = base64.b64encode(enc[1])
        self.saveEncrypted(encoded)
        return encoded
        
    def saveEncrypted(self, encrypted):
        fSave = open(self._SECRET_FILENAME, 'wt')
        fSave.write(encrypted.decode('utf-8'))        
        fSave.close()
        
    def readEncrypted(self):
        fSaved = open(self._SECRET_FILENAME, 'rt')
        encrypted = fSaved.read()
        fSaved.close()
        return encrypted
        
    def decrypt(self, encrypted):
        # print("Decrypt : {}".format(encrypted))        
        encBytes = base64.b64decode(encrypted)
        # print("Bytes : {}".format(encBytes))
        dec = oscrypto.symmetric.aes_cbc_pkcs7_decrypt(self.key, encBytes, self.iv)
        # print("DEC : {}".format(dec))
        return dec

if __name__ == "__main__":
    pyed = PyEncDec()
    # print(pyed.show())
    # passw = getpass.getpass()
    # rc = pyed.encrypt(passw)
    # print("Encrypted: {}".format(rc))
    sec = pyed.readEncrypted()
    # print("Encrypted: {}".format(sec))
    orig = pyed.decrypt(sec)
    print(orig)
