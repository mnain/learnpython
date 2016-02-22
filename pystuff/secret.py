#!/usr/bin/env python

import os

BLOCK_SIZE=32
secret = os.urandom(BLOCK_SIZE)
for i in range(BLOCK_SIZE):
	print i,hex(ord(secret[i]))
