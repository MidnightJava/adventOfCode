'''
Created on Jan 11, 2019

@author: maleone
'''
from __future__ import print_function
import re
import sys

all_bots = {}
max_bot = None
max_sig = 0
seen = set()

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
def test_coord(loc, bots):
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


def move_loc(loc, bot):
	global all_bots
	total_d = sum([abs(bot[i] - loc[i]) for i in range(3)])
	target_d = abs(total_d) - abs(all_bots[bot])
	dx = bot[0] - loc[0]
	dy = bot[1] - loc[1]
	dz = bot[2] - loc[2]
	r = float(total_d) / float(target_d)
	x = int(loc[0] + (dx / r) - 3)
	y = int(loc[1] + (dy / r) - 3)
	z = int(loc[2] + (dz / r) - 3)
	seen_count = len(seen)
	test_coord((x,y,z), all_bots)
	if len(seen) >= seen_count:
		return (x,y,z)
	else:
		return None

min_d = sys.maxint
def find_bots(loc):
	global seen
	global min_d
	global all_bots
	not_seen = set(all_bots.keys()) - seen
	not_seen = sorted(not_seen, key = lambda x: all_bots[x])
	ret = None
	for bot in not_seen:
		new_loc = move_loc(loc, bot)
		if new_loc:
			ret = new_loc
			d = sum([abs(int(x)) for x in new_loc])
			min_d = min(min_d, d)
# 			print('new loc: %s  d: %d' % (new_loc, d))
	print('%d bots in range  %d bots left' % (len(seen), len(set(all_bots.keys()) - seen)))
	return ret


def search(loc):
	global seen
	global all_bots
	test_coord(loc, all_bots)
	done = False
	while not done:
		not_seen = set(all_bots.keys()) - seen
		ns_count = len(not_seen)
		if loc: loc = find_bots(loc)
		if len(not_seen) == ns_count:
			done = True
			break
	dist, coord = best_best_coord(best_coords[1])
	print(dist, coord, best_coords[0], len(best_coords[1]), len(seen))

	# correct answer is min d plus one, taking min of all distances, regardless of number of bot hits
	# Doesn't make sense, maybe a lucky guess
	print('min distance:', min_d)

# search((0,0,0))
search((17736794, 59893573, 29250847))

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


