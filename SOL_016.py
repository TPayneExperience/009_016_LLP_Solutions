#!/usr/bin/env python

# -- 1 --
class AutoIncrementSinglton(object):
	_instance = None
	def __new__(self, *args, **kwargs):
		if not self._instance:
			self._instance = super(AutoIncrementSinglton, 
				self).__new__(self)
			self.value = 0
		self.value += 1
		return self.value


## ---------------------------------------
# -- 2 --
def Singleton(myClass):
	instances = {}
	def GetInstance(*args, **kwargs):
		if myClass not in instances:
			instances[myClass] = myClass(*args, **kwargs)
		return instances[myClass]
	return GetInstance

@Singleton
class PhonebookManager(object):
	def __init__(self):
		self.myDict = {}
	def AddEntry(self, name, number, *args, **kwargs):
		self.myDict[name] = number
	def GetEntry(self, name, *args, **kwargs):
		if name in self.myDict.keys():
			return self.myDict[name]
		return '000-000-0000'


##======================================
if __name__ == '__main__':
	print (AutoIncrementSinglton())
	print (AutoIncrementSinglton())
	print (AutoIncrementSinglton())

	pm = PhonebookManager()
	pm.AddEntry('tomithy', '555-555-5555')
	pm2 = PhonebookManager()
	print (pm2.GetEntry('tomithy'))
















