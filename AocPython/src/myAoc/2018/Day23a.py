'''
Created on Jan 11, 2019

@author: maleone
'''
from __future__ import print_function
import re
import sys
import math

all_bots = {}
max_bot = None
max_sig = 0
seen = set()
tested_locs = set()

with open('data/Day23') as f:
	for l in f:
		vals = []
		for v in l.split(','):
			vals.append(int(re.sub(r'[^\d\-]', '', v)))
		all_bots[((vals[0], vals[1], vals[2]))] = vals[3]


		if vals[3] > max_sig:
			max_sig = vals[3]
			max_bot = (vals[0], vals[1], vals[2])

in_range = 0
for bot in all_bots.keys():
	if abs(bot[0] - max_bot[0]) + abs(bot[1] - max_bot[1]) + abs(bot[2] - max_bot[2]) <= all_bots[max_bot]:
		in_range += 1

print('Part 1:', in_range)

def in_range(loc, bot):
	d = sum([abs(bot[i] - loc[i]) for i in range(3)])
	return d <= all_bots[bot]


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
def test_coord(loc, bots, track=True):
	global tested_locs
	if track: tested_locs.add(loc)
	x, y, z = loc
	global best_coords
	global prev_dist
	global count
	global seen
	hits = 0
	new_seen = set()

	for bot, d in bots.iteritems():
		if (abs(bot[0] - x) + abs(bot[1] - y) + abs(bot[2] - z)) <= d:
			hits += 1
			new_seen.add(bot)
	if hits == best_coords[0]:
		best_coords[1].append((x, y, z))
		seen = set(new_seen)
	elif hits > best_coords[0]:
		best_coords = (hits, [(x, y, z)])
		seen = set(new_seen)
	# Uncomment this to get the initial coordinate to pass to search
# 	dist, coord = best_best_coord(best_coords[1])
# 	if dist != prev_dist:
# 		print(dist, coord, best_coords[0], len(best_coords[1]), len(seen))
# 		prev_dist = dist

def findVec(point1,point2):
	finalVector = [0 for coOrd in point1]
	for dimension, coOrd in enumerate(point1):
		deltaCoOrd = point2[dimension]-coOrd
		finalVector[dimension] = deltaCoOrd
	return finalVector


def move_loc(loc, bot):
	global all_bots
	total_d = sum([abs(bot[i] - loc[i]) for i in range(3)])
	target_d = abs(total_d) - abs(all_bots[bot])
	
	vec = findVec(loc, bot)
	if target_d <= 0:
		test_coord(loc, all_bots)
		ret = loc
	else:
		r = abs(float(total_d) / float(target_d))
		for i in range(3):
			vec[i] = loc[i] + int(math.ceil(vec[i]/r)) + (1 if vec[i] >= 0 else -1)
		test_coord(tuple(vec), all_bots)
		ret = tuple(vec)
# 		for j in xrange(1, int(r), 1000):
# 			for i in range(3):
# 				vec[i] = loc[i] + int(math.ceil(vec[i]/j)) + (1 if vec[i] >= 0 else -1)
# 			test_coord(tuple(vec), all_bots)
	return ret
		
min_d = sys.maxint
def find_bots(loc):
	global seen
	global min_d
	global all_bots
	not_seen = set(all_bots.keys()) - seen
	not_seen = sorted(not_seen, key = lambda x: sum([abs(x[i] - loc[i]) for i in range(3)]) / all_bots[x])
# 	not_seen = sorted(not_seen, key = lambda x: all_bots[x], reverse=True)
	for bot in not_seen:
		loc = move_loc(loc, bot)
		d = sum([abs(int(x)) for x in loc])
		min_d = min(min_d, d)
# 			print('new loc: %s  d: %d' % (new_loc, d))
	print('%d bots in range  %d bots left' % (len(seen), len(set(all_bots.keys()) - seen)))
	return loc


def search(loc):
	global seen
	global all_bots
	global tested_locs
	test_coord(loc, all_bots)
	done = False
	while not done:
		not_seen = set(all_bots.keys()) - seen
		ns_count = len(not_seen)
		loc = find_bots(loc)
		if len(not_seen) == ns_count:
			done = True
			break
	dist, coord = best_best_coord(best_coords[1])
	print(dist, coord, best_coords[0], len(best_coords[1]), len(seen))
	print('Tested %d locs' % len(tested_locs))
	not_seen = set(all_bots.keys()) - seen
	incr = 10000
	for bot in not_seen:
		for loc in sorted(tested_locs, key = lambda x: sum([abs(x[i] - loc[i]) for i in range(3)])  / all_bots[bot]):
			loc = list(loc)
			while not in_range(tuple(loc), bot):
				for i in range(3):
					direc = 1 if bot[i] > loc[i] else -1
					loc[i]+= incr*direc
					test_coord(tuple(loc), all_bots, False)
			dist, coord = best_best_coord(best_coords[1])
			print(dist, coord, best_coords[0], len(best_coords[1]), len(seen))

	# correct answer is min d plus one, taking min of all distances, regardless of number of bot hits
	# Doesn't make sense, maybe a lucky guess
	print('min distance:', min_d)

search((0,0,0))
# search(all_bots.keys()[0])
# search((17736794, 59893573, 29250847))

def minDistance(n, k, point):
	# Sorting points in all dimension
	p = zip(*point)
	point2 = []

	for i in range(k):
		point2.append(sorted(p[i]))

	res = []
	for i in range(k):
		res.append(point2[i][((n + 1) / 2) - 1])

# 	return res

	test_coord(res, all_bots)

	# This gets us a coordinate in range of 870 bots
	res = []
	point_range = [  ((n + 1) / 2) - 250, ((n + 1) / 2) + 50 ]
	for i in xrange(point_range[0], point_range[1]):
		for j in xrange(point_range[0], point_range[1]):
			for k in xrange(point_range[0], point_range[1]):
				res = (point2[0][i], point2[1][j], point2[2][k])
				test_coord(res, all_bots)
	print(res, end=" ")

#Use this to get initial coordinate (in range of 870 bots) to pass to search
# minDistance(1000, 3, all_bots.keys())

# Part 1: 580
# Part2 target: 97816347 (978 bots) not 106944840


