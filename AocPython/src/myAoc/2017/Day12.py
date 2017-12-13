'''
Created on Dec 12, 2017

@author: Mark
'''
from _collections import defaultdict

d = defaultdict(set)
group = set()
global rawgroups
rawgroups = []
groups = []

def addItems(d, items, group):
	orig = set(group)
	for item in items:
		group.add(item.strip())
		for k,v in d.items():
			if k.strip() == item.strip():
				group.update(v)
			if item.strip() in v:
				group.add(k.strip())
	rawgroups.append(set(group))
# 	if len(groups) == 0:
# 		groups.add(".".join(group))
# 	else:
# 		found = False
# 		for g_s in groups:
# 			g = set(g_s.split('.'))
# 			if g & group:
# 				g.update(group)
# 				groups.remove(g_s)
# 				g_s = ".".join(g)
# 				groups.add(g_s)
# 				found = True
# 				break
# 		if not found:
# 			groups.add(".".join(group))
	return group - orig

with open("data/Day12") as f:
	for line in f:
		parts = line.strip().split('<->')
		l = parts[1].strip().split(',')
		l = map(lambda x: x.strip(), l)
		d[parts[0].strip()].update(l)
		for x in l:
			d[x.strip()].add(parts[0].strip())

added = addItems(d, ['0'], group)
while len(added) > 0:
	added = addItems(d, added, group)

print "Part 1:", len(group)

# for k,v in d.items():
# 	group.clear()
# 	added = addItems(d, [k], group)
# 	while len(added) > 0:
# 		added = addItems(d, added, group)

for rg in rawgroups:
	for p in rg:
		found = False
		for g in groups:
			if p in g:
				found = True
				g.update(rg)
				break
		if not found:
			groups.append(rg)

print "Part 2:", len(groups)
