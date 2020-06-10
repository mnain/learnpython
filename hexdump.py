#!/usr/bin/env python

""" testurls.py """

import os
import sys

def hexDumpFile(fname):
    # print fname
    if os.path.exists(fname):
        block = open(fname,'rb').read()
        # print(type(block))
        # print(len(block))
        indx = 0
        charBlock = []
        blockCount = 0
        for i in block:
            if indx == 0:
              print("{:04d} ".format(blockCount), end=' ')
              blockCount += 16
            print("{:02x} ".format(i), end=' ')
            c = "{:c}".format(i)
            if c >= ' ' and c <= '~':
              charBlock.append(c)
            else:
              charBlock.append(' ')
            indx += 1
            if indx == 16:
                print(str(charBlock))
                # print(' ')
                charBlock = []
                indx = 0
        print(" ")
    else:
        print(fname,"not found")

if __name__ =="__main__":
    hexDumpFile(sys.argv[1])
