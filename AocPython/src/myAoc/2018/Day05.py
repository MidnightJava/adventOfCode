'''
Created on Dec 5, 2018

@author: maleone
'''
import re
import time

def solve(s):
	i = 0
	while (i < len(s) - 1):
		if s[i] == s[i+1].swapcase():
			s = s[:i] + s[i+2:]
			i-=1
		else:
			i+= 1
	return s


with open('./data/Day05') as f:
	start_time = time.time()
	s = f.read()
	print "Part 1:", len(solve(s))
	li = []
	for c in list('abcdefghijklmnopqrstuvwxyz'):
		length = len(solve(re.sub(r"["+ c + c.upper() + ']', '', s)))
		li.append(length)
	print "Part 2:", min(li)
	print("--- %s seconds ---" % (time.time() - start_time))

# Part 1: 10584
# Part 2: 6968

