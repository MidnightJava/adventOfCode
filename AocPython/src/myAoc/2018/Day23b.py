'''
Created on Jan 11, 2019

@author: maleone
'''
from __future__ import print_function
import re
import sys
import time
from __builtin__ import False, True

bots = {}
bot_list = []
max_bot = None
total_sig = 0
max_sig = 0
seen = set()

with open('data/Day23') as f:
	for l in f:
		vals = []
		for v in l.split(','):
			vals.append(int(re.sub(r'[^\d\-]', '', v)))
		bots[((vals[0], vals[1], vals[2]))] = vals[3]
		bot_list.append(vals[3])
		total_sig += vals[3]


		if vals[3] > max_sig:
			max_sig = vals[3]
			max_bot = (vals[0], vals[1], vals[2])

in_range = 0
for bot in bots.keys():
	if abs(bot[0] - max_bot[0]) + abs(bot[1] - max_bot[1]) + abs(bot[2] - max_bot[2]) <= bots[max_bot]:
		in_range += 1

print('Part 1:', in_range)

def get_bounds(bots):
	max_bounds = [0, 0, 0]
	min_bounds = [sys.maxint, sys.maxint, sys.maxint]
	for bot in bots:
		max_bounds[0] = max(max_bounds[0], bot[0])
		max_bounds[1] = max(max_bounds[1], bot[1])
		max_bounds[2] = max(max_bounds[2], bot[2])
		min_bounds[0] = min(min_bounds[0], bot[0])
		min_bounds[1] = min(min_bounds[1], bot[1])
		min_bounds[2] = min(min_bounds[2], bot[2])
	return min_bounds, max_bounds


def best_best_coord(best_coords):
	best = None
	d = sys.maxint
	for c in best_coords:
		new_d = abs(c[0]) + abs(c[1]) + abs(c[2])
		if  new_d < d:
			d = new_d
			best = c
	return d, best


best_coords = (0, [])  # num in range, list of coords with that number in range
prev_dist = 0
count = 0


# def test_coord(loc):
# 	x, y, z = loc
# 	global best_coords
# 	global prev_dist
# 	global count
# 	global seen
# 	hits = 0
# 	new_seen = set()
# 	for bot, d in bots.iteritems():
# 		if abs(bot[0] - x) + abs(bot[1] - y) + abs(bot[2] - z) <= d:
# 			hits += 1
# 			new_seen.add(bot)
# 	if hits == best_coords[0]:
# 		best_coords[1].append((x, y, z))
# 		seen = set(new_seen)
# 	elif hits > best_coords[0]:
# 		best_coords = (hits, [(x, y, z)])
# 		seen = set(new_seen)

def test_coord(loc, bots):
	x, y, z = loc
	global best_coords
	global prev_dist
	global count
	global seen
	hits = 0
	new_seen = set()

	for bot, d in bots.iteritems():
		if abs(bot[0] - x) + abs(bot[1] - y) + abs(bot[2] - z) <= d:
			hits += 1
			new_seen.add(bot)
	if hits == best_coords[0]:
		best_coords[1].append((x, y, z))
		seen = set(new_seen)
	elif hits > best_coords[0]:
		best_coords = (hits, [(x, y, z)])
		seen = set(new_seen)

	dist, coord = best_best_coord(best_coords[1])
# 	if dist != prev_dist:
	print(dist, coord, best_coords[0], len(best_coords[1]), len(seen))
# 		prev_dist = dist


search_range = 100
search_start = (36972649, 67835632, 37037487)
start_time = time.time()


def minDistance(n, k, point):
	p = zip(*point)
	point2 = []

	for i in range(k):
		point2.append(sorted(p[i]))
	res = []
	for i in range(k):
		res.append(point2[i][((n + 1) / 2) - 1])

	print(res)
	test_coord(res, bots)
	res = []
	point_range = [  ((n + 1) / 2) - 250, ((n + 1) / 2) + 50 ]
	for i in xrange(point_range[0], point_range[1]):
		for j in xrange(point_range[0], point_range[1]):
			for k in xrange(point_range[0], point_range[1]):
				res = (point2[0][i], point2[1][j], point2[2][k])
				test_coord(res, bots)
	print(res, end=" ")

# This gets us a coordinate in range of 870 bots
# minDistance(1000, 3, bots.keys())

def move_loc(loc, main_bounds, bounds):
	min_m, max_m = main_bounds
	min_b, max_b = bounds

	# tets if x overlaps
	if min_b[0] >= min_m[0] and min_b[0] <= max_m[0]:
		x = min(max_b[0], max_m[0])
	elif max_b[0] >= min_m[0] and max_b[0] <= max_m[0]:
		x = min(max_b[0], max_m[0])
	else :
		return None

	#test if y overlaps
	if min_b[1] >= min_m[1] and min_b[1] <= max_m[1]:
		y = min(max_b[1], max_m[1])
	elif max_b[1] >= min_m[1] and max_b[1] <= max_m[1]:
		y = min(max_b[1], max_m[1])
	else :
		return None

	#test if z overlaps
	if min_b[2] >= min_m[2] and min_b[2] <= max_m[2]:
		z = min(max_b[2], max_m[2])
		return (x,y,z)
	elif max_b[2] >= min_m[2] and max_b[2] <= max_m[2]:
		z = min(max_b[2], max_m[2])
		return (x,y,z)
	else :
		return None


def find_bots(loc, inrange, outside):
	x,y,z = loc

	for bot in outside:
		main_bounds = get_bounds(inrange)
		bounds = get_bounds([bot])
		new_loc = move_loc(loc, main_bounds, bounds)
		if new_loc:
			print('new loc', new_loc, sum([abs(x) for x in new_loc]))
			x,y,z = new_loc
			inrange.add(bot)
	new_bots = {}
	for b in inrange:
		new_bots[b] = bots[b]
	test_coord((x,y,z), new_bots)


def search(loc):
	global seen
	global bots
	test_coord(loc, bots)
	done = False
# 	while not done:
	not_seen = set(bots.keys()) - seen
	ns_count = len(not_seen)
	find_bots(loc, seen, not_seen)
	not_seen = set(bots) - seen
# 	if len(not_seen) == ns_count:
# 		done = True
# 		break
	dist, coord = best_best_coord(best_coords[1])
	print(dist, coord, best_coords[0], len(best_coords[1]), len(seen))


search((17736794, 59893573, 29250847))

# Part 1: 580
# Part2 target: 97816347 (978 bots)


