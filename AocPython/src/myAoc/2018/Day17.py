'''
Created on Dec 18, 2018

@author: Mark
'''
import re
from collections import defaultdict

def get_next_floor(x, y):
	for i in xrange(y, max_y + 1):
		if i in floors:
			for seg in floors[i]:
				if seg[0] <= x and seg[1] >= x:
					return (i, seg[0], seg[1])
	return None

def get_next_wall_right(x, y, _max):
	for i in xrange(x, max_x + 1):
		if i and i > _max:
			break
		if i in walls:
			for seg in walls[i]:
				if seg[0] <= y and seg[1] >= y:
					return (i, seg[0], seg[1])
	return None

def get_next_wall_left(x, y, _min):
	for i in xrange(x, min_x-1, -1):
		if i and i < _min:
			break
		if i in walls:
			for seg in walls[i][::-1]:
				if seg[0] <= y and seg[1] >= y:
					return (i, seg[0], seg[1])
	return None

def get_wall_top(x,y):
	wall = walls[x]
	for seg in wall:
		if seg[1] == y: return seg[0]
	return None

def flow(x, y):
	global count
	if y >= max_y: return
	floor = get_next_floor(x, y)
	if floor is not None:
		level = floor[0]
		print "floor %d  x: %d" % (level, x)
		left = floor[1]
		right = floor[2]
		tl = get_wall_top(left, level)
		tr = get_wall_top(right, level)
		for i in xrange(y+1, level):
			r = get_next_wall_right(x, i, right)
			if r: r = r[0]
			l = get_next_wall_left(x, i, left)
			if l: l = l[0]
			if not r and not l:
				count+= 1
			elif r and not l:
				incr = (r - left + 1)
				count+= incr
			elif l and not r:
				incr = (right - l + 1)
				count+= incr
			elif l and r:
				incr = (r - l - 1)
				count+= incr
		if tl < tr:
			count+= (level - tr + 2)
			if level+1 < max_y:
				flow(right+1, level+1)
		elif tl > tr:
			count+= (level - tl + 2)
			if level+1 < max_y:
				flow(left-1, level+1)
		else:
			if tr: count+= (level - tr + 2)
			if tl: count+= (level - tl + 2)
			count+= (right - left)
			if level+1 < max_y:
				flow(right+1, level+1)
				flow(left-1, level+1)
	
				

floors = defaultdict(list)
walls = defaultdict(list)

p = r'(\w)=(\d+), (\w)=(\d+)\.\.(\d+)'
max_y = 0
min_x = 1000000
max_x = 0
count = 0
with open('./data/Day17') as f:
	for scan in f:
		m = re.search(p, scan.strip())
		if m:
			if m.group(1) == 'y':
				floors[int(m.group(2))].append( (int(m.group(4)), int(m.group(5))) )
				if int(m.group(2)) > max_y: max_y = int(m.group(2))
				if int(m.group(5)) > max_x: max_x = int(m.group(5))
				if int(m.group(4)) < min_x: min_x = int(m.group(4))
			elif m.group(1) == 'x':
				walls[int(m.group(2))].append( (int(m.group(4)), int(m.group(5))) )
# 				if int(m.group(5)) > max_y: max_y = int(m.group(5))
				if int(m.group(2)) > max_x: max_x = int(m.group(2))
				if int(m.group(2)) < min_x: min_x = int(m.group(2))

	for k,v in floors.items():
		floors[k] = sorted(floors[k], key=lambda x: x[0])

# 	for k,v in floors.iteritems():
# 		print 'at level %d: %s' % (k, v)

	for k,v in walls.items():
		walls[k] = sorted(walls[k], key=lambda x: x[0])
		
# print get_wall_top(504, 13)
flow(500, 0)
print "Part 1:", count
# print get_next_floor(500, 1800)
#
# 	for k,v in walls.iteritems():
# 		print 'at x %d: %s' % (k, v)

print "max y: %d\tmin x: %d\tmax x: %d" % (max_y, min_x, max_x)
# 
# for x,y in [(494,1), (495,1), (498,1), (505, 1), (506,0), (495, 11), (499,9)]:
# 	print 'floor at %d,%d: %s' % (x,y ,get_next_floor(x, y))
# print
# 	
# for x,y, _max in [(496,1, 501), (496, 2, 501), (496,3, 501), (498, 6, 501), (500,9, None), (502, 11, 504), (506,11, 504)]:
# 	print 'wall to right at %d,%d: %s' % (x,y ,get_next_wall_right(x, y, _max))
# print
# 
# for x,y, _min in [(496,1, 495), (496, 2, 495), (496,3, 495), (498, 6, 495), (500,9, None), (502, 11, 498), (506,11, 498)]:
# 	print 'wall to left at %d,%d: %s' % (x,y ,get_next_wall_left(x, y, _min))
# print



