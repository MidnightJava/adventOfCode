'''
Created on Jan 11, 2019

@author: maleone
'''
from __future__ import print_function
import re
import sys

bots = {}
max_bot = None
max_sig = 0

with open('data/Day23') as f:
	for l in f:
		vals = []
		for v in l.split(','):
			vals.append(int(re.sub(r'[^\d\-]','', v)))
		bots[((vals[0], vals[1], vals[2]))] = vals[3]
		if vals[3] > max_sig:
			max_sig = vals[3]
			max_bot = (vals[0], vals[1], vals[2])

in_range = 0
for bot in bots.keys():
	if abs(bot[0] - max_bot[0]) + abs(bot[1] - max_bot[1]) + abs(bot[2] - max_bot[2]) <= bots[max_bot]:
		in_range+= 1

print('Part 1:', in_range)

def best_best_coord(best_coords):
	best = None
	d = sys.maxint
	for c in best_coords:
		new_d = abs(c[0]) + abs(c[1]) + abs(c[2])
		if  new_d < d:
			d = new_d
			best = c
	return d, best


best_coords = (0, []) # num in range, list of coords with that number in range
prev_dist = 0
# count = 0
def test_coord(x, y, z):
	global best_coords
	global prev_dist
	global count
# 	if count % 10000 == 0:
# 		print('testing %d, %d, %d' % (x,y,z))
# 	count+= 1
	hits = 0
	for bot, d in bots.iteritems():
		if abs(bot[0] - x) + abs(bot[1] - y) + abs(bot[2] - z) <= d:
			hits+= 1
	if hits == best_coords[0]:
		best_coords[1].append((x, y, z))
	elif hits > best_coords[0]:
		best_coords = (hits, [(x,y,z)])

# 	if (12, 12, 12) in best_coords[1]:
# 		print(best_coords)

# 	print(len(best_coords[1]))
	dist, coord = best_best_coord(best_coords[1])
	if dist != prev_dist:
		print(dist, coord, len(best_coords[1]))
		prev_dist = dist
# 	if dist == 36:
# 		sys.exit()

search_range = 100
search_start = (0,0,0)
# while True:
# 	for x in xrange(search_start[0], search_start[0] + search_range):
# 		for i in [-1, 1]:
# 			for bot in bots:
# 				test_coord(bot[0] + x*i, bot[1] + search_start[1], bot[2] + search_start[2])
# 	for y in xrange(search_start[1], search_start[1] + search_range):
# 		for i in [-1, 1]:
# 			for bot in bots:
# 				test_coord(bot[0] + search_start[0], bot[1] + y*i, bot[2] + search_start[2])
# 	for z in xrange(search_start[2], search_start[2] + search_range):
# 		for i in [-1, 1]:
# 			for bot in bots:
# 				test_coord(bot[0] + search_start[0], bot[1] + search_start[1], bot[2] + z*i)
#
# 	search_start = (search_start[0] + search_range, search_start[1] + search_range, search_start[2] + search_range)

def minDistance(n, k, point):
	# Sorting points in all dimension
	p = zip(*point)
	point2 = []

	for i in range(k):
		point2.append(list(p[i]))

	for i in range(k):
			point2[i].sort()

	# Output the required k points
	res = []
	for i in range(k):
		res.append(point2[i][((n + 1) // 2) - 1])
		print(res, end =" ")

	print()
	print(abs(res[0]) + abs(res[1]) + abs(res[2]))

minDistance(1000, 3, bots.keys())


# Part 1: 580
# Part 2: 114124710 too high not 114124611 (199 bots max)
# Part2 target: 97816347 (978 bots)

