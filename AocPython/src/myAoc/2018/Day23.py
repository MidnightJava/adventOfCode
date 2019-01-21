'''
Created on Jan 11, 2019

@author: maleone
'''
from __future__ import print_function
import re
import sys

all_bots = {}
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
	if sum([abs(bot[i] - max_bot[i]) for i in range(3)]) <= all_bots[max_bot]:
		in_range += 1

print('Part 1:', in_range)


def best_best_coord():
	global best_coords
	best = None
	d = sys.maxint
	for c in best_coords[1]:
		new_d = sum([abs(c[i]) for i in range(3)])
		if  new_d < d:
			d = new_d
			best = c
	return d, best


# num in range, list of coords with that number in range
best_coords = (0, [])

def test_coord(loc):
	x, y, z = loc
	global best_coords
	global seen
	hits = 0
	new_seen = set()
	seen_length = len(seen)

	for bot, d in all_bots.iteritems():
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


def next_loc(loc, bot):
	global all_bots
	total_d = sum([abs(bot[i] - loc[i]) for i in range(3)])
	target_d = abs(total_d) - abs(all_bots[bot])
	
	vec = findVec(loc, bot)
	if target_d <= 0:
		test_coord(loc)
		ret = loc
	else:
		r = abs(float(total_d) / float(target_d))
		for i in range(3):
			vec[i] = loc[i] + int(vec[i]/r) + (1 if vec[i] >= 0 else -1)
		test_coord(tuple(vec))
		ret = tuple(vec)
	return ret

def bot_sort(loc):
	def f(bot):
		return sum([abs(bot[i] - loc[i]) for i in range(3)]) / all_bots[bot]
	return f
		
def find_bots(loc):
	global seen
	global min_d
	global all_bots
	not_seen = set(all_bots.keys()) - seen
	not_seen = sorted(not_seen, key = bot_sort(loc) )
	for bot in not_seen: loc = next_loc(loc, bot)
	return loc


def search(loc):
	loc = find_bots(loc)
	_, coord = best_best_coord()
	not_seen = set(all_bots.keys()) - seen
	not_seen = sorted(not_seen, key = bot_sort(loc))
	for bot in not_seen:
		d = sum([abs(bot[i] - loc[i]) for i in range(3)])
		vec = findVec(loc, bot)
		for i in range(3):
			vec[i] = coord[i] + int(vec[i] / float(d)) + (1 if vec[i] >= 0 else -1)
		for j in range(2):
			for k in range(2):
				for l in range(2):
					for m in [-1,1]:
						vec[0]+= (j*m); vec[1]+= (k*m); vec[2]+= (l*m)
						test_coord(vec)
		
	dist, coord = best_best_coord()
	print('Part 2: %d' % dist)
	print('%d bots in range at %s' %  (len(seen), coord))

search((0,0,0))

# Part 1: 580
# Part2: 97816347 (978 bots in range)


