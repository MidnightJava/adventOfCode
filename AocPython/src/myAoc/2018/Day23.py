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
maxcoords = [0, 0, 0]
mincoords = [sys.maxint, sys.maxint, sys.maxint]
seen = set()

with open('data/Day23') as f:
	for l in f:
		vals = []
		for v in l.split(','):
			vals.append(int(re.sub(r'[^\d\-]', '', v)))
		bots[((vals[0], vals[1], vals[2]))] = vals[3]
		bot_list.append(vals[3])
		total_sig += vals[3]
		maxcoords[0] = max(maxcoords[0], vals[0])
		maxcoords[1] = max(maxcoords[1], vals[1])
		maxcoords[2] = max(maxcoords[2], vals[2])
		mincoords[0] = min(mincoords[0], vals[0])
		mincoords[1] = min(mincoords[1], vals[1])
		mincoords[2] = min(mincoords[2], vals[2])
		
		if vals[3] > max_sig:
			max_sig = vals[3]
			max_bot = (vals[0], vals[1], vals[2])

in_range = 0
for bot in bots.keys():
	if abs(bot[0] - max_bot[0]) + abs(bot[1] - max_bot[1]) + abs(bot[2] - max_bot[2]) <= bots[max_bot]:
		in_range += 1

print('Part 1:', in_range)


def best_best_coord(best_coords):
	best = None
	d = sys.maxint
	for c in best_coords[1]:
		new_d = abs(c[0]) + abs(c[1]) + abs(c[2])
		if  new_d < d:
			d = new_d
			best = c
	return d, best


best_coords = (0, [])  # num in range, list of coords with that number in range
prev_dist = 0
count = 0


def test_coord(loc):
	x, y, z = loc
	global best_coords
	global prev_dist
	global count
	global seen
# 	if count % 10000 == 0:
# 		print('testing %d, %d, %d' % (x,y,z))
# 	count+= 1
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

# 	dist, coord = best_best_coord(best_coords[1])
# 	if dist != prev_dist:
# 		print(dist, coord, best_coords[0], len(best_coords[1]), len(seen))
# 		prev_dist = dist
# 		if dist == 97816347:
# 			print('%d seconds' % (time.time() - start_time))
# 			sys.exit()


search_range = 100
search_start = (36972649, 67835632, 37037487)
start_time = time.time()
# while True:
# 	for x in xrange(search_start[0], search_start[0] + search_range):
# 		for i in [-1, 1]:
# 			for bot in bots:
# 				test_coord((bot[0] + x*i, bot[1] + search_start[1], bot[2] + search_start[2]))
# 	for y in xrange(search_start[1], search_start[1] + search_range):
# 		for i in [-1, 1]:
# 			for bot in bots:
# 				test_coord((bot[0] + search_start[0], bot[1] + y*i, bot[2] + search_start[2]))
# 	for z in xrange(search_start[2], search_start[2] + search_range):
# 		for i in [-1, 1]:
# 			for bot in bots:
# 				test_coord((bot[0] + search_start[0], bot[1] + search_start[1], bot[2] + z*i))
# 
# 	search_start = (search_start[0] + search_range, search_start[1] + search_range, search_start[2] + search_range)


def minDistance(n, k, point):
	# Sorting points in all dimension
	p = zip(*point)
	point2 = []

	for i in range(k):
		point2.append(sorted(p[i]))
		
# 	for i in range(k):
# 		l = point2[i]
# 		for j in xrange(len(l)):
# 			if l[j] <= 0:
# 				l[j]+= (bot_list[j] / max_sig * abs(maxcoords[i] - mincoords[i]))
# 			else:
# 				l[j]-= (bot_list[j] / max_sig * abs(maxcoords[i] - mincoords[i]))
			
	res = []
	for i in range(k):
		res.append(point2[i][((n + 1) / 2) - 1])
		
	return res
	
# 	test_coord(res)
# 			
# 	# This gets us a coordinate in range of 870 bots
# 	res = []
# 	point_range = [  ((n + 1) / 2) - 250, ((n + 1) / 2) + 50 ]
# 	for i in xrange(point_range[0], point_range[1]):
# 		for j in xrange(point_range[0], point_range[1]):
# 			for k in xrange(point_range[0], point_range[1]):
# 				res = (point2[0][i], point2[1][j], point2[2][k])
# 				test_coord(res)
# 	print(res, end=" ")
		
# 	print(res, end =" ")

	print()
# 	print(math.floor(abs(res[0]) + abs(res[1]) + abs(res[2])))


# minDistance(1000, 3, bots.keys())

def weight_by_signal(i):
	def f(x):
		if x <= 0:
			x+= (bot_list[i] / max_sig * abs(maxcoords[i] - mincoords[i]))
		else:
			x-= (bot_list[i] / max_sig * abs(maxcoords[i] - mincoords[i]))
		return x
	return f

def add_bots(n, point):
	p = zip(*point)
	point2 = []

	for i in range(3):
		point2.append(list(p[i]))
		
# 	for i in range(3):
# 		l = point2[i]
# 		for j in xrange(len(l)):
# 			if l[j] <= 0:
# 				l[j]+= (bot_list[j] / max_sig * abs(maxcoords[i] - mincoords[i]))
# 			else:
# 				l[j]-= (bot_list[j] / max_sig * abs(maxcoords[i] - mincoords[i]))
				
	for i in range(3):
		point2[i] = sorted(point2[i], key= weight_by_signal(i), reverse=True)
	
	for i in xrange(n):
		for j in xrange(n):
			for k in xrange(n):
				res = (point2[0][i], point2[1][j], point2[2][k])
				test_coord(res)

def search(loc):
	global seen
	global bots
	test_coord(loc)
	done = False
	while not done:
		not_seen = set(bots) - seen
		ns_count = len(not_seen)
		add_bots(len(not_seen), not_seen)
		not_seen = set(bots) - seen
		if len(not_seen) == ns_count:
			done = True
			break
	print(best_best_coord(best_coords))

search((17736794, 59893573, 29250847))

# Part 1: 580
# Part 2: 114124710 too high not 114124611 (199 bots max)
# Part2 target: 97816347 (978 bots)

# Output the required k points
# res = []
# for i in range(k):
# 	a = point2[i][((n + 1) / 2) - 114]
# 	b = point2[i][((n + 1) / 2)]
# 	res.append((a + b) / 2 + 42362)
# print(res, end =" ")
# 106881214 (17736794, 59893573, 29250847) 870 1 870
