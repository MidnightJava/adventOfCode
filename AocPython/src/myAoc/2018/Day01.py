'''
Created on Nov 30, 2018

@author: Mark
'''

from collections import defaultdict

freq = 0
with open('./data/Day01') as f:
	freq = sum([int(x) for x in f])
	print "Part 1:", freq
	
	
freq = 0
fd = defaultdict(int)
fd[0] = 1
found = False
while not found:
	with open('./data/Day01') as f:
			for s in f:
				freq+= int(s)
				fd[freq]+= 1
				if fd[freq] == 2:
					print "Part 2:", freq
					found = True
					break
#Part 1: 505
#Part 2: 72330
