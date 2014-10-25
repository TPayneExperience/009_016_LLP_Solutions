#!/usr/bin/env python

import os.path

path = (os.path.dirname(os.path.realpath(__file__)))

words = "You know what this file could use?"
words += '\nHam'*50

# -- C --
for i in range(5):
	# -- A --
	f = open('%03d_myFile.html'%i, 'w')
	# -- B --
	f.write(words)
	f.close()

print ('done!')

