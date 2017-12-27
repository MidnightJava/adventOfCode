'''
Created on Dec 26, 2017

@author: Mark
'''
from _collections import defaultdict

count = 0

class state:
	
	def __init__(self, write, move, nxt):
		self.write = write
		self.move = move
		self.next = nxt
		
line = defaultdict(int)
curr = 0
ones = set()
states = {
	"A" : [state(1,1,'B'), state(1,-1,'E')],
	"B" : [state(1,1,'C'), state(1,1,'F')],
	"C" : [state(1,-1,'D'), state(0,1,'B')],
	"D" : [state(1,1,'E'), state(0,-1,'C')],
	"E" : [state(1,-1,'A'), state(0,1,'D')],
	"F" : [state(1,1,'A'), state(1,1,'C')],
	}

state = states["A"]
for i in xrange(12459852):
	idx = line[curr]
	line[curr] = state[idx].write
	if line[curr] == 1:
		if not curr in ones:
			count+=1
			ones.add(curr)
	else:
		if curr in ones:
			count-= 1
			ones.remove(curr)
	curr+= state[idx].move
	state = states[state[idx].next]
	
print "Part 1:", count	