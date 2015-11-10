#!/usr/bin/python

class Learn:
	def __init__(s):
		print("init Learn")

	def method1(s,arg1):
		print("method1 Learn",arg1)

if __name__ == "__main__":
	l = Learn()
	l.method1(50)
