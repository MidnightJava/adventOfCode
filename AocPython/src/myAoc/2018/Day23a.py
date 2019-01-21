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
	seen_length = len(seen)

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
	return len(seen) > seen_length

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
	return ret
		
def find_bots(loc):
	global seen
	global min_d
	global all_bots
	not_seen = set(all_bots.keys()) - seen
	not_seen = sorted(not_seen, key = lambda x: sum([abs(x[i] - loc[i]) for i in range(3)]) / all_bots[x])
	for bot in not_seen:
		loc = move_loc(loc, bot)
	print('%d bots in range  %d bots left' % (len(seen), len(set(all_bots.keys()) - seen)))
	return loc


def search(loc):
	global seen
	global all_bots
	global tested_locs
	global not_seen
	global coord
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
	not_seen = sorted(not_seen, key = lambda x: sum([abs(x[i] - coord[i]) for i in range(3)])  - all_bots[x])
	ns_count = 0
	ns_count = len(not_seen)
	bot_count = 0
	for bot in not_seen:
		coord = list(coord)
		total_d = sum([abs(bot[i] - coord[i]) for i in range(3)])
		
		vec = findVec(loc, bot)
		for i in range(3):
			vec[i] = coord[i] + int(math.ceil(vec[i]) / float(total_d)) + (1 if vec[i] >= 0 else -1)
		for j in range(2):
			for k in range(2):
				for l in range(2):
					vec[0]-= j
					vec[1]-= k
					vec[2]-= l
					test_coord(vec, all_bots, False)
					print(sum([abs(vec[i]) for i in range(3)]))
					if test_coord(tuple(vec), all_bots): break
		
# 		dist, coord = best_best_coord(best_coords[1])
		print('BOT: %d' % bot_count)
		print('\tresults', dist, coord, best_coords[0], len(best_coords[1]), len(seen))
		bot_count+= 1
	not_seen = set(all_bots.keys()) - seen
	not_seen = sorted(not_seen, key = lambda x: sum([abs(x[i] - loc[i]) for i in range(3)]) / all_bots[x])

search((0,0,0))

# Part 1: 580
# Part2: 97816347 (978 bots in range)


