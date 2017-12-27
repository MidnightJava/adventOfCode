'''
Created on Dec 26, 2017

@author: Mark
'''
from _collections import defaultdict


comps = []
hiscore = None
longest = defaultdict(list)

with open("data/Day24") as f:
	for l in f:
		comp = l.strip().split("/")
		comps.append((int(comp[0]), int(comp[1])))

def solve(bridge, used):
	global comps
	global hiscore
	global longest
	for c in comps:
		tip = bridge[len(bridge) - 1]
		if c in used:
			continue
		if tip[1] == c[0]:
			bridgec = bridge[::]
			bridgec.append([c, c[1]])
			usedc = set(used)
			usedc.add(c)
			solve(bridgec, usedc)
		elif tip[1] == c[1]:
			bridgec = bridge[::]
			bridgec.append([c, c[0]])
			usedc = set(used)
			usedc.add(c)
			solve(bridgec, usedc)
		score = 0
		for x in bridge:
			c = x[0]
			score+= c[0]
			score+= c[1]
		if hiscore is None or hiscore < score:
			hiscore = score
		longest[len(bridge)].append(score)
		

	
for comp in comps:
	bridge = []
	used = set()
	if 0 in [comp[0], comp[1]]:
		if comp[0] == 0:
			bridge.append([comp, comp[1]])
			used.add(comp)
			solve(bridge[::], set(used))
		else:
			bridge.append([comp, comp[0]])
			used.add(comp)
			solve(bridge[::], set(used))
		score = 0
		for x in bridge:
			c = x[0]
			score+= c[0]
			score+= c[1]
		if hiscore is None or hiscore < score:
			hiscore = score
		longest[len(bridge)].append(score)
		
print "Part 1", hiscore
print "Part 2:", max(longest[max(longest.keys())])
