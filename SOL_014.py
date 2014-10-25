#!/usr/bin/env python

# -- 1 -- 		Not So Good Solution
def ListWithinListPrinter (outerList, *args, **kwargs):
	for innerList in outerList:
		for item in innerList:
			print (item)


# -- 2 & 3 -- 	Better, almost there!
def RecursiveListPrinter(outerList, *args, **kwargs):
	if outerList and type(outerList) == list:
		for innerList in outerList:
			if type(innerList) == list:
				RecursiveListPrinter(innerList)
			else:
				print (innerList)


# -- 4 -- 		WORTHY OF HAM!
def BestRecursiveListPrinter(*args, **kwargs):
	for outerList in list(args) + list(kwargs.values()):
		if type(outerList) == list:
			for innerList in outerList:
				if type(innerList) == list:
					BestRecursiveListPrinter(innerList)
				else:
					print (innerList)


##======================================
if __name__ == '__main__':
	L1 = [[1,2],[3,4]]
	L2 = [[[1], 3], [4, 5]]
	L3 = [[[32, [234, '', 'HAM', [42342], 
			[345], 3456, 4576], 456, 100], 555]]

	ListWithinListPrinter(L1, L1, L1)
	RecursiveListPrinter(L2)
	BestRecursiveListPrinter(L1, L2, myList = L3)

	print ("You're a sexy beast!")
