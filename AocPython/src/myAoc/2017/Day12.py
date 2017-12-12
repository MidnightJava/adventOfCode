'''
Created on Dec 12, 2017

@author: Mark
'''
from _collections import defaultdict

global d
d = defaultdict(list)
global group
group = set()

def getItems(k):
	s = set()
	s.add(k)
	if len(d[k]) > 0:
		for x in d[k]:
			if not x in group:
				group.update(getItems(x))
	return s
	
with open("data/Day12") as f:
	for line in f:
		parts = line.strip().split('<->')
		l = parts[1].strip().split(',')
		d[parts[0].strip()].extend(l)
		for x in l:
			d[x.strip()].append(parts[0].strip())
		
group.add('0')
group.update(d['0'])
for x in d['0']:
	group.update(getItems(x))
	
print len(group)
