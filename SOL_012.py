#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

# class Human(metaclass=ABCMeta): ## python 3.x
class Human(object):			## remove for python 3.x
	__metaclass__ = ABCMeta		## remove for python 3.x
	@abstractmethod
	def __init__(self):
		pass

	def run(self):
		print ('running!')

# class Robot(metaclass=ABCMeta): ## python 3.x
class Robot(object): 			## remove for python 3.x
	__metaclass__ = ABCMeta		## remove for python 3.x
	@abstractmethod
	def __init__(self):
		pass
	def vacuum(self):
		print ('vacuuming!')

class Cyborg(Human, Robot):
	def __init__(self):
		super(Cyborg, self).__init__()


##======================================
if __name__ == '__main__':
	try:
		h = Human()
	except:
		print ('Could not create a Human.')
	try:
		r = Robot()
	except:
		print ('Could not create a Robot.')

	c = Cyborg()
	c.run()
	c.vacuum()
