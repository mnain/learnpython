#!/usr/bin/env python

import random

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
