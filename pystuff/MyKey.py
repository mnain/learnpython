#!/usr/bin/env python

import random
import os

class MyKey:

    def __init__(self):
        self.homeDir = os.environ['HOME']
        fname = ".key"
        self.keyFileName = self.homeDir + os.sep + fname
        self.keyLen = 256
        self.key = random.getrandbits(self.keyLen)
        self.strKey = hex(self.key)[2:-1]
        if os.path.exists(self.keyFileName) == False:
            self.update()
        else:
            self.strKey = self.read()

    def __str__(self):
        return "<MyKey:%d, %s>" % (self.key,self.strKey)

    def get(self):
        return self.strKey

    def getKeyFileName(self):
        return self.keyFileName

    def update(self):
        fh = open(self.getKeyFileName(), 'wt')
        fh.writelines(self.strKey)
        fh.close()

    def read(self):
        fh = open(self.getKeyFileName(), 'rt')
        line = fh.readline()
        fh.close()
        self.strKey = line.rstrip()
        return line.rstrip()

if __name__ == "__main__":
    mk = MyKey()
    print mk.read()
