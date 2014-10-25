#!/usr/bin/env python

import SOL_011_Base as Base

class BetterX(Base.Base):
	def __init__(self):
		self.x = 17

class BetterHam(Base.Base):
	def __init__(self):
		super(BetterHam, self).__init__()
	def printHam(self):
		print ('Ham2')

class Combo(BetterX, BetterHam):
	def __init__(self):
		super(Combo, self).__init__()


##======================================
if __name__ == '__main__':
	c = Combo()
	c.printHam()
	print (c.x)
	print (Base.Base.__subclasses__())