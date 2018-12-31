'''
Created on Dec 20, 2018

@author: maleone
'''
from __future__ import print_function
import re
from _collections import defaultdict

class Rect:

	def __init__(self):
		self.tl = None
		self.bl = None
		self.br = None
		self.tr = None

def print_basin(bas):
	print('TL: %s BL: %s, BR: %s, TR: %s, Box: %s' % (bas.tl, bas.bl, bas.br, bas.tr, bas.box))

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
# Is the point x,y inside the box represented by bas (including the border)
def in_box(bas, x, y):
	if bas.box:
		bas_top = min(bas.br[1], bas.bl[1])
		bas_bottom = bas.tr[1]
	else:
		bas_top = min(bas.tr[1], bas.tl[1])
		bas_bottom = bas.br[1]
	return x in range(bas.bl[0], bas.br[0]+1) and y in range(bas_bottom, bas_top +1)

# Is the point x,y in the border of the box represented by bas
def in_box_border(bas, x, y):
	if bas.box:
		return (x in range(bas.bl[0], bas.br[0]+1) and y in [bas.tr[1], bas.br[1]]) or (x in [bas.bl[0], bas.br[0]] and y in [bas.tr[1], bas.br[1]])
	else:
		return (x in range(bas.bl[0], bas.br[0]+1) and y == bas.br[1]) or (x == bas.br[0] and y in range(bas.tr[1], bas.br[1]+1)) or (x == bas.bl[0] and y in range(bas.tl[1], bas.bl[1]+1))

# Get any box that is partially or wholly inside the box represented by bas
def get_inner_box_loc(bas):
	rec = Rect()
	pts = defaultdict(list)
	for y in xrange(min(bas.tl[1], bas.tr[1]) - 1, bas.br[1]):
		for x in xrange(bas.bl[0] + 1, bas.br[0]):
			if (x,y) in clay: pts[y].append(x)
	if len(pts) == 0: return None
	top = min(pts.keys())
	bottom = max(pts.keys())
	rec.tl = (min(pts[top]), top)
	rec.tr = (max(pts[top]), top)
	rec.bl = (min(pts[bottom]), bottom)
	rec.br = (max(pts[bottom]), bottom)
	rec.box = True if len(pts[rec.tl[1]]) == len(pts[rec.bl[1]]) else False
	return rec

# Get the first basin found below the point x,y
def get_next_basin(x, y):
	global grid
	rect = Rect()
	while (x,y) not in clay:
		y+= 1
		if y > max_y:
			return 0
	if (x-1,y) not in clay:
		#We hit the vertical side of a basin
		return None
	# We reached the bottom of a basin or the top of a closed box
	else:
		while (x, y) in clay:
			x-= 1
		x+= 1
	rect.bl = (x, y)
	if (x, y-1) in clay:
		#The wall goes up, so it's a basin
		vsense = -1
		rect.box = False
	elif (x, y+1) in clay:
		#The wall goes down, so it's a box
		vsense = 1
		rect.box = True
		
	#Now we map out the walls and get the three remaining corner locations
	while (x,y) in clay:
		y+= vsense
	rect.tl = (x, y - vsense)
	x = rect.bl[0]
	y = rect.bl[1]
	while (x,y) in clay:
		x+= 1
	x-= 1
	rect.br = (x, y)
	while (x,y) in clay:
		y+= vsense
	rect.tr = (x, y-vsense)
	return rect

max_y = 0
min_x = 1000000
min_y = 1000000
max_x = 0

def flow(x, y, rnum):
	
	global grid
	if y >= max_y or (x,y) in flowing:
		return
	
	bas = get_next_basin(x, y)
	if bas is None:
# 		This means we hit the vertical edge of a basin when trying to find the next one below us
#		So we move down to it and then flow down on either side of it
		while (x,y) not in clay:
			grid[(x,y)] = '|'
			if y >= min_y:
				flowing.add((x, y))
			y+= 1
			if y >= max_y:
				return
		flow(x+1, y-1, rnum+1)
		flow(x-1, y-1, rnum+1)
		return
	elif bas == 0:
		# We did not find a basin below us, so we just flow to the end of the grid
		while y <= max_y:
			grid[(x,y)] = '|'
			if y >= min_y:
				flowing.add((x, y))
			y+= 1
		return
	floor = bas.bl[1]

	while (x, y+1) not in clay:
		if y >= min_y:
			flowing.add((x, y))
		grid[(x,y)] = '|'
		y+= 1
		if y == max_y:
			return
	if not bas.box:
		y-= 1
		innerBox = get_inner_box_loc(bas)
		if not innerBox or (innerBox.tr[1] > max(bas.tr[1], bas.tl[1]) and innerBox.br[1] > max(bas.tr[1], bas.tl[1])):
			# no inner box or one contained wholly within the basin
			
			if bas.tl[1] == bas.tr[1]:
				sym = True
				depth = bas.bl[1] - bas.tl[1] #walls are same height
			else:
				sym = False
				depth = min(bas.bl[1] - bas.tl[1], bas.br[1] - bas.tr[1])
			y+= 1
			for i in xrange(depth):
				for x in xrange(bas.bl[0]+1, bas.br[0]):
					if innerBox and innerBox.box:
						# Inner box is a closed box
						if not in_box(innerBox, x, y):
							rest.add((x, y))
							try:
								if (x,y) in flowing: flowing.remove((x,y))
							except:
								pass
							grid[(x,y)] = '~'
					elif innerBox:
						# Inner box is a basin
						if not in_box_border(innerBox, x, y):
							rest.add((x, y))
							try:
								if (x,y) in flowing: flowing.remove((x,y))
							except:
								pass
							grid[(x,y)] = '~'
					else:
						# No inner box
						rest.add((x, y))
						try:
							if (x,y) in flowing: flowing.remove((x,y))
						except:
							pass
						grid[(x,y)] = '~'
				y-= 1
			if sym:
				# Flows over on both sides
				for x in xrange(bas.tl[0]-1, bas.tr[0]+2):
					if y >= min_y: flowing.add((x, y))
					grid[(x,y)] = '|'
				for i in xrange(depth+2):
					if y < max_y:
						if y >= min_y: flowing.add((bas.bl[0]-1, y))
						grid[(bas.bl[0]-1, y)] = '|'
						if y >= min_y: flowing.add((bas.br[0]+1, y))
						grid[(bas.br[0]+1, y)] = '|'
						y+= 1
					else:
						return

				flow(bas.bl[0]-1,y, rnum+1)
				flow(bas.br[0]+1,y, rnum+1)
			else:
				if bas.tl[1] < bas.tr[1]:
					#flows to right
					for x in xrange(bas.tl[0]+1, bas.tr[0]+2):
						if y >= min_y: flowing.add((x, y))
						grid[(x,y)] = '|'
					for i in xrange(depth+3):
						if y <= max_y:
							if y >= min_y: flowing.add((bas.tr[0]+1, y))
							grid[(bas.tr[0]+1,y)] = '|'
							y+= 1
					if y < max_y:
						flow(bas.br[0]+1,y, rnum+1)
				else:
					#flows to left
					for x in xrange(bas.tl[0]-1, bas.tr[0]):
						if y >= min_y: flowing.add((x, y))
						grid[(x,y)] = '|'
					for i in xrange(depth+3):
						if y <= max_y:
							if y>= min_y: flowing.add((bas.bl[0]-1, y))
							grid[(bas.bl[0]-1, y)] = '|'
							y+= 1
					if y < max_y:
						flow(bas.bl[0]-1,y, rnum+1)
		else:
			#has inner box that protrudes above basin
			
			if innerBox.tr[1] < min(bas.tr[1], bas.tl[1]):
				if x > innerBox.tr[0]:
					#flow to right of innerBox
					depth = bas.br[1] - bas.tr[1]# -1
					divideDepth = bas.br[1] - innerBox.br[1] - 1
					y+= 1
					for i in xrange(depth):
						for x in xrange(bas.bl[0]+1, bas.br[0]):
							if i < divideDepth or x > innerBox.br[0]:
								rest.add((x, y))
								if (x,y) in flowing: flowing.remove((x,y))
								grid[(x,y)] = '~'
						y-= 1
					
					for x in xrange(innerBox.tr[0]+1, bas.tr[0]+2):
						if y >= min_y: flowing.add((x, y))
						grid[(x,y)] = '|'
					for i in xrange(depth+3):
						if y < max_y:
							if y >= min_y: flowing.add((bas.tr[0]+1, y))
							grid[(bas.tr[0]+1,y)] = '|'
							y+= 1
					if y < max_y:
						flow(bas.br[0]+1,y, rnum+1)
				elif x < innerBox.bl[0]:
					#flows to left
					depth = bas.bl[1] - bas.tl[1]
					divideDepth = bas.bl[1] - innerBox.bl[1] -1
					y+= 1
					for i in xrange(depth):
						for x in xrange(bas.bl[0]+1, bas.br[0]):
							if i < divideDepth or x < innerBox.bl[0]:
								rest.add((x, y))
								if (x,y) in flowing: flowing.remove((x,y))
								grid[(x,y)] = '~'
						y-= 1
					
					for x in xrange(bas.tl[0]-1, innerBox.tl[0]):
						if y >= min_y: flowing.add((x, y))
						grid[(x,y)] = '|'
					for i in xrange(depth+3):
						if y < max_y:
							if y >= min_y: flowing.add((bas.tl[0]-1, y))
							grid[(bas.tl[0]-1,y)] = '|'
							y+= 1
					if y < max_y:
						flow(bas.bl[0]-1,y, rnum+1)
	else:
		#Just skip over the box and find the next floor below it
		flow(x, y+(bas.tl[1] - bas.bl[1]) + 2, rnum+1)

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
				if int(m.group(2)) > max_y: max_y = int(m.group(2))
				if int(m.group(2)) < min_y: min_y = int(m.group(2))
				if int(m.group(5)) > max_x: max_x = int(m.group(5))
				if int(m.group(4)) < min_x: min_x = int(m.group(4))
			elif m.group(1) == 'x':
				for i in xrange( int(m.group(4)), int(m.group(5)) + 1 ):
					grid[(int(m.group(2)), i)] = '#'
					clay.add((int(m.group(2)), i))
				if int(m.group(2)) < min_x: min_x = int(m.group(2))
				if int(m.group(2)) > max_x: max_x = int(m.group(2))
				if int(m.group(5)) > max_y: max_y = int(m.group(5))
				if int(m.group(4)) < min_y: min_y = int(m.group(4))
global count
count = 0
total = 0
flow(500, 1, 1)
# print_grid()
part1 = 0
part2 = 0
for y in xrange(min_y, max_y + 1):
		for x in xrange(min_x-2, max_x+ 2):
			if (x,y) in grid:
				if grid[(x,y)] == '~':
					part1+= 1
					part2+= 1
				if  grid[(x,y)] == '|':
					part1+= 1
print("Part1: %d, Part2: %d" % (part1, part2))

# Part 1: 39649
# Part 2: 28864
