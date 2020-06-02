#!/usr/bin/env python

import sys
import random
import re
import getopt

_TEMPLATE = 'Aa99,,9A,aa9A,9'
_TEMPLATE_GEN = 'Aa9,'
_PASSLEN = 20
_DIGITS = "0123456789"
_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_LOWER = "abcdefghijklmnopqrstuvwxyz"
#_PUNCT = ".,!%&-+/*:#{}()[]~;"
_PUNCT = ",.!%&$-+/*@:~#"
_CHARSET = _DIGITS + _UPPER + _LOWER + _PUNCT

def generateTemplate(length):
	#print "Generate Template:",length
	validTemplate = False
	while not validTemplate:
		template = 'A'
		for i in range(length-2):
			oneChar = _TEMPLATE_GEN[random.randrange(0,len(_TEMPLATE_GEN))]
			template = template + oneChar
		template = template + 'a'
		validTemplate = checkTemplate(template)
	return template

def checkTemplate(templ):
	rc = False
	if '9' in templ and ',' in templ:
		rc = True
	return rc

def generateTemplatePassword(template):
	passwd = ''
	for i in template:
		if i == 'A':
			oneChar = _UPPER[random.randrange(0,len(_UPPER))]
			passwd = passwd + oneChar
		if i == 'a':
			oneChar = _LOWER[random.randrange(0,len(_LOWER))]
			passwd = passwd + oneChar
		if i == '9':
			oneChar = _DIGITS[random.randrange(0,len(_DIGITS))]
			passwd = passwd + oneChar
		if i == ',':
			oneChar = _PUNCT[random.randrange(0,len(_PUNCT))]
			passwd = passwd + oneChar
	return(passwd)

def generatePassword(lenth):
		num_PUNCTRequired = 2
		num_UPPERCaseRequired = 2
		num_LOWERCaseRequired = 2
		num_DIGITSRequired = 2

		_UPPERFound = 0
		_LOWERFound = 0
		_DIGITSFound = 0
		_PUNCTFound = 0
		firstChar = lastChar = 0

		min_UPPER = 2
		min_LOWER = 2
		min_DIGITS = 2
		min_PUNCT = 2

		passwd = ""

		# print("_PASSLEN=%d" % _PASSLEN)
		# print("_CHARSET=%s" % _CHARSET)
		# while _UPPERFound >= min_UPPER and _LOWERFound >= min_LOWER and _DIGITSFound >= min_DIGITS and _PUNCTFound >= min_PUNCT:
		while firstChar == 0 and lastChar == 0 and _UPPERFound <= min_UPPER and _LOWERFound <= min_LOWER and _DIGITSFound <= min_DIGITS and _PUNCTFound <= min_PUNCT:
			passwd = ""
			for i in range(_PASSLEN):
				passwd = passwd + _CHARSET[random.randrange(0,len(_CHARSET))]
			slen = len(passwd)  
			#if passwd[0] in _UPPER or passwd[0] in _LOWER:
				#firstChar = 1
			#if passwd[slen-1] in _UPPER or passwd[slen-1] in _LOWER:
				#lastChar = 1
			if passwd[0] in _PUNCT:
				oneChar = _UPPER[random.randrange(0,len(_UPPER))]
				passwd = oneChar + passwd[1:]
				firstChar = 1
			if passwd[slen-1] in _PUNCT:
				oneChar = _LOWER[random.randrange(0,len(_LOWER))]
				passwd = passwd[0:slen-2] + oneChar
				lastChar = 1
			for i in range(len(passwd)):
				if passwd[i] in _DIGITS:
					_DIGITSFound = _DIGITSFound + 1
				if passwd[i] in _LOWER:
					_LOWERFound = _LOWERFound + 1
				if passwd[i] in _UPPER:
					_UPPERFound = _UPPERFound + 1
				if passwd[i] in _PUNCT:
					_PUNCTFound = _PUNCTFound + 1
		#print("_DIGITS %d _PUNCTuation %d _LOWER %d _UPPER %d firstC %d lastChar %d password: %s" % (_DIGITSFound,_PUNCTFound,_LOWERFound,_UPPERFound,firstChar,lastChar,passwd))
		#print("%s" % passwd)
		#print("Password: %s\n" % passwd)
		return(passwd)

if __name__ == "__main__":
	genNPasswords = 1
	toExit = 0
	genTemplate = True
	templ = None
	try:
		opts,args = getopt.getopt(sys.argv[1:], "hl:t:n:")
		for o,a in opts:
			if o == "-l":
			  _PASSLEN = int(a)
			  if _PASSLEN > 128:
				  _PASSLEN = 128
			if o == "-t":
			  templ = _TEMPLATE = a
			  genTemplate = False
			if o == "-n":
			  genNPasswords = int(a)
			if o == "-h":
			  print(""" python genpass.py [-options]
-l len
-t template
-n generate n passwords
				""")
			  toExit = 1
			  sys.exit(1)
	except:
		_PASSLEN = 14
	if toExit:
		sys.exit(0)
	#print(generatePassword(_PASSLEN))
	if genTemplate:
		templ = generateTemplate(_PASSLEN)
	while genNPasswords:
		print(generateTemplatePassword(templ))
		genNPasswords -= 1
