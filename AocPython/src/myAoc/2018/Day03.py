'''
Created on Dec 3, 2018

@author: maleone
'''

import re
from collections import defaultdict

class Rectangle:
	def __init__(self, line):
		pattern = '\#(\d+)\s+\@\s+(\d+)\,(\d+)\:\s+(\d+)x(\d+)'
		m = re.search(pattern, line)
		if m:
			self.id = m.group(1)
			self.x = int(m.group(2))
			self.y = int(m.group(3))
			self.w = int(m.group(4))
			self.h = int(m.group(5))

rectangles = []

def makeGrid(recs):
	grid = defaultdict(int)
	for rect in recs:
		for x in range(rect.x, rect.x + rect.w):
			for y in range(rect.y, rect.y + rect.h):
				grid[(x,y)]+= 1
	return grid


with open('./data/Day03') as f:
	for line in f:
		rectangles.append(Rectangle(line))

	grid = makeGrid(rectangles)
	count = len([v for v in grid.values() if v >= 2])
	print "Part 1:", count

	for rect in rectangles:
		found = True
		_id = None
		for x in range(rect.x, rect.x + rect.w):
			for y in range(rect.y, rect.y + rect.h):
				if grid[(x,y)] > 1:
					found = False;
					break;
				_id = rect.id
		if found:
			print "Part 2:", _id

# Part 1: 110195
# Part 2: 894

