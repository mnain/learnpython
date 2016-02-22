#!/usr/bin/env python

def red():
 return chr(27)+"[91m"

def green():
 return chr(27)+"[92m"

def off():
 return chr(27)+"[0m"

def cyan():
 return chr(27)+"[36m"

def yellow():
 return chr(27)+"[33m"

def blink():
 return chr(27)+"[5m"

def rred():
 return chr(27)+"[41m"

def rgreen():
 return chr(27)+"[42m"

BLACK=30
RED=31
GREEN=32
YELLOW=33
BLUE=34
MAGENTA=35
CYAN=36
WHITE=37

BG_BLACK=40
BG_RED=41
BG_GREEN=42
BG_YELLOW=43

COLORSET = [
	BLACK,
	RED,
	GREEN,
	YELLOW,
	BLUE,
	MAGENTA,
	CYAN,
	WHITE,
	]
def color(n):
 return chr(27)+"["+str(n)+"m"

if __name__ == "__main__":
 for i in range(90,108):
  print i,chr(27)+"["+str(i)+"mColor"+off()
 for i in COLORSET:
  print color(i)+str(i)+off()
 for i in COLORSET:
  print color(i+10)+str(i+10)+off()
 print rred()+"RED"+off()
 print rgreen()+"GREEN"+off()
