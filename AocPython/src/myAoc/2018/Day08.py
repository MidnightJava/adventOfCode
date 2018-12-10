'''
Created on Dec 8, 2018

@author: Mark
'''

def solve1(l, counter):
	children = l.pop(0)
	meta = l.pop(0)
	for i in xrange(children):
		solve1(l, counter)
	for i in xrange(meta):
		counter['sum']+= l.pop(0)
	return counter['sum']
	
def solve2(l):
	_sum = 0
	child_count = l.pop(0)
	meta = l.pop(0)
	if child_count > 0:
		children = []
		for i in xrange(child_count):
			children.append(solve2(l))
		for i in xrange(meta):
			idx = l.pop(0)
			if idx != 0 and idx-1 < len(children):
				_sum+= children[idx-1]
	else:
		for i in xrange(meta):
			_sum+= l.pop(0)
	return _sum
	
	
with open('./data/Day08') as f:
	l = map(int, f.read().split())
	l2 = l[:]
	print "Part 1:", solve1(l, {'sum':0})
	print "Part 2:", solve2(l2)
	
#Part 1: 46578
#Part 2: 31251