'''
Created on Dec 18, 2018

@author: Mark
'''
import re
from collections import defaultdict

floors = defaultdict(list)
walls = defaultdict(list)

p = r'(\w)=(\d+), (\w)=(\d+)\.\.(\d+)'
with open('./data/Day17') as f:
	for scan in f:
		m = re.search(p, scan.strip())
		if m:
			if m.group(1) == 'y':
				floors[int(m.group(2))].append( ( int(m.group(4)), int(m.group(5))  - int(m.group(4)) + 1 ) )
			elif m.group(1) == 'x':
				walls[int(m.group(2))].append( ( int(m.group(4)), int(m.group(5))  - int(m.group(4)) + 1 ) )
	
	for k,v in floors.items():
		floors[k] = sorted(floors[k], key=lambda x: x[0])
			
	for k,v in floors.iteritems():
		print 'at level %d: %s' % (k, v)
		
	for k,v in walls.items():
		walls[k] = sorted(walls[k], key=lambda x: x[0])
			
	for k,v in walls.iteritems():
		print 'at x %d: %s' % (k, v)