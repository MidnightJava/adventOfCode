'''
Created on Jan 2, 2019

@author: Mark
'''
from __future__ import print_function
from collections import deque

def BFS(x, y, seen):
		queue = deque( [(x,y,0)])
		while len(queue)>0:
			x,y,d = queue.popleft()
			if (x,y) not in grid: continue
			if grid[(x,y)] == '.': grid[(x,y)]='*' #for visualization
			neighbors = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if (n[0],n[1]) in grid]
			seen[(x,y)] = d
			for nb in neighbors:
				if not nb in seen or seen[(nb[0], nb[1])] > d:
					if grid[(nb[0], nb[1])] == '.': d = d + 1
					queue.append((nb[0],nb[1],d))

def get_opts(inp):
	lpcount = 0
	i = 0
	sub = ''
	subs = []
	while i < len(inp):
		c = inp[i]
		if lpcount == 0:
			if c == '|':
				subs.append(sub)
				sub = ''
			else:
				if c == '(': lpcount+= 1
				elif c == ')': lpcount-= 1
				sub+= c
		else:
			if c == '(': lpcount+= 1
			elif c == ')': lpcount-= 1
			sub+= c
		i+= 1
	if len(sub): subs.append(sub)
	return subs

def parse(inp, loc, tail=None):
	global grid
	i = 0
	lpcount = 0
	x = loc[0]
	y = loc[1]
	sub = ''
	while i < len(inp):
		c = inp[i]
		if lpcount:
			if c == '(': lpcount+= 1
			elif c == ')':
				lpcount-= 1
				if lpcount == 0:
					[parse(opt, (x,y), inp[i+1:]) for opt in get_opts(sub)]
					i = len(inp)
					continue
			sub+= c
		else:
			if c == '(': lpcount+= 1
			elif c == 'N':
				grid[(x,y-1)] = '-'
				grid[(x,y-2)] = '.'
				y-= 2
			elif c == 'S':
				grid[(x,y+1)] = '-'
				grid[(x,y+2)] = '.'
				y+= 2
			elif c == 'W':
				grid[(x-1,y)] = '|'
				grid[(x-2,y)] = '.'
				x-= 2
			elif c == 'E':
				grid[(x+1,y)] = '|'
				grid[(x+2,y)] = '.'
				x+= 2
		i+= 1

	if tail is not None: parse(tail, (x,y))

inp = open('./data/Day20').read()

grid = {(0,0) : 'X'}

parse(inp[1:-2], (0,0))

minx = maxx = miny = maxy = 0

for loc in grid.iterkeys():
	minx = min(minx, loc[0])
	maxx = max(maxx, loc[0])
	miny = min(miny, loc[1])
	maxy = max(maxy, loc[1])

seen = {}
BFS(0, 0, seen)
print("Part 1", max(seen.values()))
print("Part 2", len([seen[x] for x in seen.keys() if seen[x] >= 1000 and grid[(x[0],x[1])] == '*']))

# for y in xrange(miny-1, maxy+2, 1):
# 	for x in xrange(minx-1, maxx+2, 1):
# 		if x == 0 and y == 0: print('X', end='')
# 		elif (x,y) in grid: print(grid[x,y], end='')
# 		else: print('#', end='')
# 	print()

# Part 1: 3469
# Part 2: 8780
