#!/usr/bin/env python
#
# example of class heirarchy in Python
#

class Foo:
	x = -1
	def __init__(self, v):
		print dir(self)
		self.x = v

	def show(self):
		return self.x

class Bar(Foo):
	y = -1
	def __init__(self, v):
		Foo.__init__(self,v)
		print dir(self)
		self.y = v

	def show(self):
		return str(Foo.show(self)) + " " + str(self.y)

if __name__ == "__main__":
	f = Foo(3)
	print f.show()
	b = Bar(20)
	print b.show()
