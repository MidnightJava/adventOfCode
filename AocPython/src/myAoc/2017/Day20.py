'''
Created on Dec 19, 2017

@author: Mark
'''
from _collections import defaultdict
import collections
from numpy import float32, int32
import re


parts = []
aves = defaultdict(lambda: defaultdict(int))
cum_aves = {}

for line in open("data/Day20").read().split('\n'):
	m = re.match(r"^p\=\<(-?\d+)\,(-?\d+)\,(-?\d+)\>\,\sv\=\<(-?\d+)\,(-?\d+)\,(-?\d+)\>\,\sa\=\<(-?\d+)\,(-?\d+)\,(-?\d+)\>$", line.strip())
	p, v, a = m.group(1,2,3), m.group(4,5,6), m.group(7,8,9)
	parts.append([p, v, a])
	
# while True:
# 	for i in xrange(len(parts)):
# 		part = parts[i]
# 		p,v,a = map(lambda x: (int(x[0]), int(x[1]), int(x[2])), part)
# 		part[1] = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
# 		v = part[1]
# 		part[0] = (p[0] + v[0], p[1] + v[1], p[2] + v[2])
# 		p = part[0]
# 		md = abs(int(p[0])) + abs(int(p[1])) + abs(int(p[2]))
# 		aves[i]['cnt']+= 1
# 		aves[i]['tot']+= md
# 		aves[i]['ave'] = aves[i]['tot']/aves[i]['cnt']
# 		cum_aves[i] = aves[i]['ave']
# 		print min(cum_aves, key = cum_aves.get)
		

totaldiff = 0
while True:
	seen = []
	seenMap = defaultdict(list)
	for i in xrange(len(parts)):
		part = parts[i]
		p,v,a = map(lambda x: (int32(x[0]), int32(x[1]), int32(x[2])), part)
		part[1] = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
		v = part[1]
		part[0] = (p[0] + v[0], p[1] + v[1], p[2] + v[2])
		#results in 578 (int and Decimal) and 570 (float)
		seen.append(str(part[0][0]) + str(part[0][1]) + str(part[0][2]))
		seenMap[str(part[0][0]) + str(part[0][1]) + str(part[0][2])].append(i)
		#Results in 579
# 		seen.append(part[0])
# 		seenMap[part[0]].append(i)
	dups = [item for item, count in collections.Counter(seen).items() if count > 1]
	diff =  (len(dups) - (len(seen) - len(set(seen))))
	totaldiff += diff
	print diff
	for dup in dups:
		toremove = []
		for idx in seenMap[dup]:
			toremove.append(parts[idx])
		for p in toremove:
			parts.remove(p)
			
	print len(parts)
	if len(parts) == 578:
		break

print totaldiff
#part 2: 578 too high NOT 576 NOT 577 NOT 570