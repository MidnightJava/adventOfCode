'''
Created on Dec 6, 2018

@author: maleone
'''

from collections import defaultdict

left = 1000
right = 0
top = 1000
bottom = 0
def mdist(a,b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

with open('./data/Day06') as f:
	nodes = []
	infinite_area_nodes = set()
	grid = defaultdict(tuple)
	node_areas = defaultdict(int)
	for l in f:
		pt = map(lambda x: int(x), l.strip().split(','))
		nodes.append((int(pt[0]), int(pt[1])))
		if pt[0] < left: left = pt[0]
		if pt[0] > right: right = pt[0]
		if pt[1] < top: top = pt[1]
		if pt[1] > bottom: bottom = pt[1]
		
	for x in xrange(left, right +1):
		for y in xrange(top, bottom +1):
			if (x,y) in nodes:
				grid[(x,y)] = (x,y)
				if x == left or x == right or y == top or y == bottom:
					if (x,y) in nodes:
						infinite_area_nodes.add((x,y))
			else:
				for node in nodes:
					if grid[(x,y)] and mdist((x,y), node) == mdist((x,y), grid[(x,y)]):
						grid[(x,y)] = (-100, -100)
					elif not grid[(x,y)] or mdist((x,y), node) < mdist((x,y), grid[(x,y)]):
						grid[(x,y)] = node
						
	for x in xrange(left, right +1):
		for y in xrange(top, bottom +1):
			if x == left or x == right or y == top or y == bottom:
# 				if (x,y) == grid[(x,y)]:
					infinite_area_nodes.add(grid[(x,y)])
	
	finite_area_nodes = set(nodes) - infinite_area_nodes				
		
	for x in xrange(left, right +1):
		for y in xrange(top, bottom +1):
			if grid[(x,y)] in finite_area_nodes:
				node_areas[grid[(x,y)]]+= 1
			
	print "Part 1:", max(node_areas.values());
	
	region_count = 0
	for x in xrange(left, right+1):
		for y in xrange(top, bottom+1):
			count = 0
			for node in nodes:
				count+= mdist((x,y), node)
			if count < 10000: region_count+= 1
	print "Part 2:", region_count
	

#Part 1: 4171
#Part 2: 39545
			
			