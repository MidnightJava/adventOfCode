'''
Created on Dec 1, 2018

@author: Mark
'''
from collections import defaultdict
from __builtin__ import int

twos = 0
threes = 0
seen = []
with open('./data/Day02') as f:
	for line in f:
		line = line.strip()
		d = defaultdict(int)
		for s in line:
			d[s]+= 1
		vals = d.values()
		if 2 in vals:
			twos+= 1
		if 3 in vals:
			threes+=1
		seen.append(line)
	print "Part 1:", twos * threes
		
#Part 2
done = False
for i in xrange(len(seen)):
	if not done:
		for j in xrange(len(seen)):
			if not done:
				l1 = seen[i]
				l2 = seen[j]
				miss = 0
				if i != j:
					miss = 0
					common = ''
					for a in xrange(len(l1)):
						if l1[a] != l2[a]:
							miss+=1
						else:
							common+= l1[a]
				if miss == 1:
					print "Part 2:", common
					done = True
					break
			
# 6672, 5506, 5016
#lujnogabetpmsydyfcovzixaw