'''
Created on Jan 2, 2019

@author: Mark
'''
from __future__ import print_function

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
				sub+= c
		else:
			if c == '(': lpcount+= 1
			elif c == ')':
				lpcount-= 1
				if lpcount == 0:
					subs.append(sub)
					sub = ''
				else:
					sub+= c
		i+= 1
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
		if c == '^':
			i+= 1
			continue
		
		if lpcount > 0:
			if c == '(': lpcount+= 1
			elif c == ')':
				if lpcount == 1:
					for opt in get_opts(sub):
						parse(opt, (x,y), inp[i:])
					i = len(inp)
					continue
				lpcount-= 1
			sub+= c
			i+= 1
		else:
			if c == '(': lpcount+= 1
			elif c == 'N':
				y-= 1
				grid[(x,y)] = '-'
				y-= 1
				grid[(x,y)] = '.'
			elif c == 'S':
				y+= 1
				grid[(x,y)] = '-'
				y+= 1
				grid[(x,y)] = '.'
			elif c == 'W':
				x-= 1
				grid[(x,y)] = '|'
				x-= 1
				grid[(x,y)] = '.'
			elif c == 'E':
				x+= 1
				grid[(x,y)] = '|'
				x+= 1
				grid[(x,y)] = '.'
			elif c == '$':
				if tail is not None: parse(tail, (x,y))
			else:
				print('Unexpected character: %s' % c)
			i+= 1
			

inp = open('./data/Day20a').read()

grid = {(0,0): 'X'}

parse(inp, (0,0))

minx = 0
maxx = 0
miny = 0
maxy = 0

for loc in grid.iterkeys():
	minx = min(minx, loc[0])
	maxx = max(maxx, loc[0])
	miny = min(miny, loc[1])
	maxy = max(maxy, loc[1])
	
print(minx, maxx, miny, maxy)
print()

for y in xrange(miny-1, maxy+1, 1):
	for x in xrange(minx-1, maxx+1, 1):
		if (x,y) in grid: print(grid[x,y], end='')
		else: print('#', end='')
	print()