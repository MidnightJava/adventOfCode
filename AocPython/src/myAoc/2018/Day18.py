'''
Created on Dec 31, 2018

@author: Mark
'''
from __future__ import print_function
from collections import defaultdict

sz = 50

def print_grid():
	global grid
	for y in xrange(sz):
		for x in xrange(sz):
			print(grid[(x,y)], end='')
		print()
		
def get_counts(grid):
	lum = 0
	tree = 0
	for y in xrange(sz):
			for x in xrange(sz):
				if grid[(x, y)] == '|': tree+= 1
				elif grid[(x,y)] == '#': lum+= 1
	return (lum, tree)
	
def transform(grid, _x, _y):
	a = grid[(_x, _y)]
	adj = []
	for y in [-1, 0, 1]:
		for x in [-1, 0, 1]:
			if not (x == 0 and y == 0) and (_x + x, _y + y) in grid:
				adj.append(grid[(_x + x, _y + y)])
	if a == '.':
		return '|' if adj.count('|') >= 3 else '.'
	elif a == '|':
		return '#' if adj.count('#') >= 3 else '|'
	elif a == '#':
		return '#' if adj.count('#') >= 1 and adj.count('|') >= 1 else '.'
	else:
		print('Unexpected grid value %s' % a)
	
with open('./data/Day18')as f:
	global grid
	grid = {}
	y = 0
	for line in f:
		x = 0
		for c in line.rstrip():
			grid[(x, y)] = c
			x+= 1
		y+= 1
		
counts = defaultdict(list)
count = 0
for i in xrange(int(1e9)):
	tot = get_counts(grid)
	tot = int(tot[0] * tot[1])
	counts[tot].append(count)
	# Totals repeat modulo 28. So find a total whose modulo-28 sequence will end at 1e9 
	if len(counts[tot]) > 2 and (1000000000 - counts[tot][0]) % 28 == 0:
		print('Part 2: %d' % tot)
		break
	new_grid = dict(grid)
	for y in xrange(sz):
		for x in xrange(sz):
			a = transform(grid, x, y)
			new_grid[(x,y)] = a
	
	grid = new_grid
	count+= 1
	if count == 10:
		tot = get_counts(grid)
		print('Part 1: %d' % int(tot[0] * tot[1]))

# Part 1 646437
# Part 2: 208080
		
