'''
Created on Dec 20, 2018

@author: maleone
'''
from __future__ import print_function
import re
import sys
import threading

sys.setrecursionlimit(20000)

class Rect:

	def __init__(self):
		self.tl = None
		self.bl = None
		self.br = None
		self.tr = None


def print_grid():
	for y in xrange(max_y + 2):
		print(str(y).zfill(4), end='')
		for x in xrange(min_x-1, max_x+ 2):
			if (x,y) in rest:
				print('~', end='')
			elif (x,y) in grid:
				print(grid[(x,y)], end='')
			else:
				print('.', end='')
		print()

def in_box(bas, x, y):
	bas_top = min(bas.tr[1], bas.tl[1])
	return x in range(bas.bl[0], bas.br[0]+1) and y in range(bas_top, bas.br[1]+1)

def get_inner_box_loc(bas):
# 	return None
	innerBoxes = set()
	for x in xrange(bas.bl[0]+1, bas.br[0]):
		inner = get_next_basin(x, min(bas.tr[1], bas.tl[1]))
# 		if inner is None: print('cant get inner box for %s, %s, %s, %s' % (bas.tl, bas.bl, bas.br,bas.tr))
		if inner and inner.bl[1] < bas.bl[1]:
			innerBoxes.add(inner)
	if len(innerBoxes) == 0:
		return None
# 	if len(innerBoxes) > 1:
# 		print("Found more than one inner box")
	return innerBoxes.pop()


def get_next_basin(x, y):
	global grid
	rect = Rect()
	while (x,y) not in clay:
		y+= 1
		if y > max_y: return 0
	if (x-1,y) not in clay and (x+1,y) not in clay:
		#We hit the vertical side of a basin
		return None
# 		while (x,y) in clay:
# 			y+=1
# 		y-= 1
# 		if (x-1,y) in clay:
# 			#we hit the right wall
# 			x-= 1
# 			while (x,y) in clay:
# 				x-=1
# 			x+=1
# 		elif (x+1,y) in clay:
# 			pass # we hit the left wall
# 		else:
# 			print('Unable to find basin bottom after hitting vertical wall')
	else:
		while (x, y) in clay:
			x-= 1
		x+= 1
	rect.bl = (x, y)
	if (x, y-1) in clay:
		vsense = -1
		rect.box = False
	elif (x, y+1) in clay:
		vsense = 1
		rect.box = True
	else:
		print('We hit a line, not a basin')
	while (x,y) in clay and y < max_y:
		y+= vsense
	rect.tl = (x, y - vsense)
	x = rect.bl[0]
	y = rect.bl[1]
	while (x,y) in clay:
		x+= 1
	x-= 1
	rect.br = (x, y)
	while (x,y) in clay and y < max_y:
		y+= vsense
	rect.tr = (x, y-vsense)
# 	if count>= 50000:
# 		print('return rect at floor %d' % rect.bl[1])
	return rect

max_y = 0
min_x = 1000000
max_x = 0

def flow(x, y):
	print_grid()
# 	print('flow from %d,%d' % (x,y))
	global count
	count+= 1
	global grid
	if y >= max_y -1: return
	bas = get_next_basin(x, y)
	if bas is None:
		if (x,y) in clay: return
		while (x,y) not in clay:
			grid[(x,y)] = '|'
			flowing.add((x, y))
			y+= 1
			if y >= max_y: return
# 		print('call flow 1', '*'*80)
		if y <= max_y:
			flow(x-1, y+1)
			flow(x+1, y+1)
		return
	elif bas == 0:
		return
	floor = bas.bl[1]
# 	if x == bas.bl[0] or x == bas.br[0]:
# 		grid[(x,y)] = '|'
# 		flowing.add((x, y))
# 		flow(x-1, y+1)
# 		flow(x+1, y+1)
# 		return
	y+= 1
	if floor > max_y: return
	while (x, y+1) not in clay:
		flowing.add((x, y))
		grid[(x,y)] = '|'
		y+= 1
		if y == max_y: return
	if y != floor-1:
		print("Expected to land at y %d. Instead landed at %d" %(floor-1, y))
		return
	if not bas.box:
		if (x, y-1) in clay:
			print('We hit clay just above basin floor')
			return
		y-= 1
		if bas.tl[1] == bas.tr[1]:
			sym = True
			depth = bas.bl[1] - bas.tl[1] #walls are same height
		else:
			sym = False
			depth = min(bas.bl[1] - bas.tl[1], bas.br[1] - bas.tr[1])
		y+= 1
		innerBox = get_inner_box_loc(bas)
		for i in xrange(depth):
			for x in xrange(bas.bl[0]+1, bas.br[0]):
				if innerBox is None or not in_box(innerBox, x, y):
					rest.add((x, y))
					if (x,y) in flowing: flowing.remove((x,y))
					grid[(x,y)] = '~'
			y-= 1
		if sym:
			for x in xrange(bas.tl[0]-1, bas.tr[0]+2):
				if innerBox is None or not in_box(innerBox, x, y):
					flowing.add((x, y))
					grid[(x,y)] = '|'
			for i in xrange(depth+2):
				if y <= max_y:
					flowing.add((bas.bl[0]-1, y))
					grid[(bas.bl[0]-1, y)] = '|'
					flowing.add((bas.br[0]+1, y))
					grid[(bas.br[0]+1, y)] = '|'
					y+= 1
# 			print_grid()
# 			print()
# 			if y <= max_y:
			flow(bas.bl[0]-1,y)
			flow(bas.br[0]+1,y)
		else:
			if bas.tl[1] < bas.tr[1]:
				#flows to right
				for x in xrange(bas.tl[0]+1, bas.tr[0]+2):
					if innerBox is None or not in_box(innerBox, x, y):
						flowing.add((x, y))
						grid[(x,y)] = '|'
				for i in xrange(depth+3):
					if y <= max_y:
						flowing.add((bas.tr[0]+1, y))
						grid[(bas.tr[0]+1,y)] = '|'
						y+= 1
				if y <= max_y:
					flow(bas.br[0]+1,y+1)
			else:
				#flows to left
				for x in xrange(bas.tl[0]-1, bas.tr[0]):
					if innerBox is None or not in_box(innerBox, x, y):
						flowing.add((x, y))
						grid[(x,y)] = '|'
				for i in xrange(depth+3):
					if y <= max_y:
						flowing.add((bas.bl[0]-1, y))
						grid[(bas.bl[0]-1, y)] = '|'
						y+= 1
				if y <= max_y:
					flow(bas.bl[0]-1,y+1)
	else:
		#Just skip over the box and find the next floor below it
		flow(x, y+(bas.tl[1] - bas.bl[1]) + 1)
# 		pass

count = 0
p = r'(\w)=(\d+), (\w)=(\d+)\.\.(\d+)'
with open('./data/Day17') as f:
	global grid
	global clay
	global rest
	global flowing
	grid = {(500, 0): '+'}
	rest = set()
	flowing = set()
	clay = set()
	for scan in f:
		m = re.search(p, scan.strip())
		if m:
			if m.group(1) == 'y':
				for i in xrange( int(m.group(4)), int(m.group(5)) + 1 ):
					grid[(i, int(m.group(2)))] = '#'
					clay.add((i, int(m.group(2))))
					if m.group(2) == '1525' : print('adding to clay %d, %s' % (i, m.group(2)))
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

# flow(500, 0)
bas = get_next_basin(502, 1518)
print('basin %s %s %s %s box: %s' % (bas.tl, bas.bl, bas.br, bas.tr, bas.box))
# inner = get_next_basin(500, 22)
# print('inner basin for (500,22): %s, %s, %s, %s' % (inner.tl, inner.bl, inner.br, inner.tr))
# bas = get_next_basin(613, 87)
# print('tl: %s bl: %s br: %s tr: %s box: %s' % (bas.tl, bas.bl, bas.br, bas.tr, bas.box))
# print_grid()
print('Part1:', len(flowing), len(rest), len(flowing) + len(rest))
# for y in xrange(0, max_y+2):
# 	print('%d:' % y, end='')
# 	for x in flowing:
# 		if x[1] == y:
# 			print('%d,' % x[0], end='')
# 	print()



# print('x from %d to %d, y from 0 to %d' % (min_x, max_x, max_y))

#Part 1: 2481 too low
