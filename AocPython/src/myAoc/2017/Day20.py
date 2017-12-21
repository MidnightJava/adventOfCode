'''
Created on Dec 19, 2017

@author: Mark
'''
from _collections import defaultdict
import re


parts = []
aves = defaultdict(lambda: defaultdict(int))
cum_aves = {}

f = open("data/Day20", "r")

for line in f:
	m = re.match(r"^p\=\<(-?\d+)\,(-?\d+)\,(-?\d+)\>\,\sv\=\<(-?\d+)\,(-?\d+)\,(-?\d+)\>\,\sa\=\<(-?\d+)\,(-?\d+)\,(-?\d+)\>$", line.strip())
	p, v, a = m.group(1,2,3), m.group(4,5,6), m.group(7,8,9)
	part = [map(lambda x: int(x), p), map(lambda x: int(x), v), map(lambda x: int(x), a)]
	parts.append(part)

part1 = True
while True:
	min_part = None
	seenMap = defaultdict(list)
	for i in xrange(len(parts)):
		part = parts[i]
		p,v,a = part[0], part[1], part[2]
		part[1] = [v[0] + a[0], v[1] + a[1], v[2] + a[2]]
		v = part[1]
		part[0] = [p[0] + v[0], p[1] + v[1], p[2] + v[2]]
		md = abs(p[0]) + abs(p[1]) + abs(p[2])
		if min_part is None or md < min_part[1]:
			min_part = (i, md)
#Not necessary to track the running average
# 		aves[i]['cnt']+= 1
# 		aves[i]['tot']+= md
# 		aves[i]['ave'] = aves[i]['tot']/aves[i]['cnt']
# 		cum_aves[i] = aves[i]['ave']
# 		lo = min(cum_aves, key = cum_aves.get)
	if part1:
		print "Part 1:", min_part[0]
# 		print "Part 1:", lo
	else:
		seen = defaultdict(list)
		for part in parts:
			k = tuple(part[0])
			seen[k].append(part)
		for k,v in seen.iteritems():
			if len(v) > 1:
				for p in v:
					parts.remove(p)
		print "Part 2:", len(parts)
