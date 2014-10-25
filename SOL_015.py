#!/usr/bin/env python

# -- 1 --
def HamMaker(*args, **kwargs):
	return 'ham'

# -- 2 --
def SandwichMaker(someFunc, *args, **kwargs):
	def SandwichMakerInside(*args, **kwargs):
		return someFunc() + ' sandwich'
	return SandwichMakerInside

# -- 3 --
@SandwichMaker
def HamMaker2(*args, **kwargs):
	return 'BETTER ham'

## ---------------------------------------
# -- 4 --
def NumMaker(*args, **kwargs):
	return 5.32

def NumAdder(someFunc, *args, **kwargs):
	def NumAdderInside(*args, **kwargs):
		return someFunc() + 5.79
	return NumAdderInside

@NumAdder
def NumMaker2(*args, **kwargs):
	return 16.43


##======================================
if __name__ == '__main__':
	Old = HamMaker
	New = SandwichMaker(HamMaker)
	New2 = HamMaker2

	print (Old(), New(), New2())

	## =============================
	
	Old = NumMaker
	New = NumAdder(NumMaker)
	New2 = NumMaker2

	print (Old(), New(), New2())
