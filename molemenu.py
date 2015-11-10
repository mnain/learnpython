#!/usr/bin/env python

import os
import sys

# moleMenuFile = '/home/mnain/mole-hosts.txt'
moleMenuFile = os.environ['HOME'] + os.sep + 'mole-hosts.txt'
global menuData
menuData = {}
global menuList
menuList = {}

def buildMenuData():
	global menuData
	allLines = open(moleMenuFile, 'rt').readlines()
	allLines = map((lambda x: x.rstrip()), allLines)
	for l in allLines:
		(h,v) = l.split('^')
		menuData[v] = h
	#print menuData
	#print menuData.keys()

def buildMenuChoices():
	global menuList
	indx = 1
	menuList[0] = 'Quit'
	for k in menuData.keys():
		menuList[indx] = k
		indx = indx + 1

def displayMenu():
	print "Select an environment:"
	for k in menuList.keys():
		print k,menuList[k]

def getChoice():
	ic = -1
	c = raw_input("Enter your choice:")
	try:
		ic = int(c)
	except:
		ic = -1
	return ic

def doSsh(host, user):
	os.command('ssh -Y '+user+'@'+host)

if __name__ == "__main__":
	hostsFile = '/home/mnain/.ssh/known_hosts'
	if os.path.exists(hostsFile):
		os.remove(hostsFile)
	buildMenuData()
	#print menuData
	#print menuData.keys()
	buildMenuChoices()
	#print menuList
	displayMenu()
	choice = -1
	while (choice not in menuList.keys()):
		choice = getChoice()
	if choice == 0:
		sys.exit(0)
	if choice in menuList.keys():
		user = os.environ['USER']
		host = menuData[menuList[choice]]
		print "Connecting to",host,"as",user
		os.system('ssh -Y '+user+'@'+host)
