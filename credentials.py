#!/usr/bin/env python

import base64
import StringIO
import pickle

LOGINKEY = 'LOGIN'
PASSWORDKEY = 'PASSWORD'

class Credentials:
	CRED = { }
	FILENAME = '.secret'
	SIO = None

	def __init__(self):
		self.SIO = StringIO.StringIO()

	def setPassword(self, user, passwd):
		self.CRED[user] = passwd

	def getPassword(self, user):
		if self.CRED.has_key(user):
			return self.CRED[user]
		else:
			return None

	def get(self):
		return self.CRED

	def set(self, login, passwd):
		self.CRED[login] = passwd

	def __repr__(self):
		return "CRED: " + repr(self.CRED)

	def write(self):
		self.SIO = StringIO.StringIO()
		self.SIO = pickle.dumps(self.CRED)
		converted = base64.b64encode(self.SIO)
		fh = open(self.FILENAME, 'wt')
		fh.writelines(converted+'\n')
		fh.close()

	def read(self):
		fh = open(self.FILENAME, 'rt')
		line = fh.readline()
		fh.close()
		orig = base64.b64decode(line)
		self.SIO = StringIO.StringIO(orig)
		self.CRED = pickle.loads(self.SIO.getvalue())

	def update(self, user, passwd):
		self.read()
		self.CRED[user] = passwd
		self.write()

if __name__ == "__main__":
	cred = Credentials()
	#cred.set('emadmin', 'Temproot!!long')
	#cred.set('ncoadmin', 'n3tc00l')
	#cred.set('db2inst1', 'db2inst1')
	#cred.write()
	cred.read()
	print cred.get()
