#!/usr/bin/python

def isPowerOf2(num):
 rc = num != 0 && (num & num -1)
 return rc

v = 15
print isPowerOf2(v)
v = 16
print isPowerOf2(v)


