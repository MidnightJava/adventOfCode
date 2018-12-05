'''
Created on Dec 5, 2018

@author: maleone
'''
import re

def boom(a, b):
	return a != b and a.upper() == b.upper()

def solve(s):
	i = 0
	while (i < len(s) - 1):
		if boom(s[i], s[i+1]):
			s = s[:i] + s[i+2:]
			i-=1
		else:
			i+= 1
	return s


with open('./data/Day05') as f:
	s = f.read()
	print "Part 1:", len(solve(s))
	li = []
	for c in list('abcdefghijklmnopqrstuvwxyz'):
		length = len(solve(re.sub(r"["+ c + c.upper() + ']', '', s)))
		li.append(length)
	print "Part 2:", min(li)

# Part 1: 10584
# Part 2: 6968

