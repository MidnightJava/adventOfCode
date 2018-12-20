'''
Created on Dec 20, 2018

@author: maleone
'''
from __future__ import print_function
import re

def print_grid():
	for y in xrange(max_y + 1):
		for x in xrange(min_x, max_x+ 1):
			if (x,y) in rest:
				print('~', end='')
			elif (x,y) in grid:
				print('#', end='')
			else:
				print('.', end='')
		print()

p = r'(\w)=(\d+), (\w)=(\d+)\.\.(\d+)'
max_y = 0
min_x = 1000000
max_x = 0

def flow(start_x, start_y):
	global count
	if start_y > max_y: return
	x = start_x
	y = start_y
	global rest
	global clay
	count+= 1
	while (x, y+1) not in rest and (x, y+1) not in clay and y+1 < max_y:
		rest.add((x, y+1))
		y+= 1
	if (x-1, y) not in rest and (x-1, y) not in clay and x-1 >= min_x:
		rest.add((x-1, y))
		flow(x-1, y)
	if (x+1, y) not in rest and (x+1, y) not in clay and x+1 <= max_x:
		rest.add((x+1, y))
		flow(x+1, y)
	if (x, y-1) not in rest and (x, y-1) not in clay and y-1 <= max_y:
		rest.add((x, y-1))
		flow(x, y-1)

count = 0
with open('./data/Day17a') as f:
	global grid
	global clay
	global rest
	global flowing
	grid = {(500, 0): '+'}
	rest = set()
	flowng = set()
	clay = set()
	for scan in f:
		m = re.search(p, scan.strip())
		if m:
			if m.group(1) == 'y':
				for i in xrange( int(m.group(4)), int(m.group(5)) + 1 ):
					grid[(i, int(m.group(2)))] = '#'
					clay.add((i, int(m.group(2))))
				if int(m.group(2)) > max_y: max_y = int(m.group(2))
				if int(m.group(5)) > max_x: max_x = int(m.group(5))
				if int(m.group(4)) < min_x: min_x = int(m.group(4))
			elif m.group(1) == 'x':
				for i in xrange( int(m.group(4)), int(m.group(5)) + 1 ):
					grid[(int(m.group(2)), i)] = '#'
					clay.add((int(m.group(2)), i))
				if int(m.group(2)) < min_x: min_x = int(m.group(2))
				if int(m.group(2)) > max_x: max_x = int(m.group(2))
				if int(m.group(5)) > max_y: max_y = int(m.group(5))
				
flow(500, 0)
print_grid()

print('x from %d to %d, y from 0 to %d' % (min_x, max_x, max_y))
