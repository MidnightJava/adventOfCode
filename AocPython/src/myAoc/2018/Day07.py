'''
Created on Dec 7, 2018

@author: maleone
'''

from collections import defaultdict

d = defaultdict(list)
orig = set()
ready = set()
res = ''

part1 = False

def getNext(l):
	global workers
	workers = []
	if part1: return l.pop(0)
	res = None
	for i in xrange(5):
		for item in l:
			ttl[item]-= 1
			ttl[item] = max(ttl[item], 0)
			if ttl[item] == 0 and res is None:
				res = item
	if res in l: l.remove(res)
	return res

def delay(c):
	return ord(c) - 4

with open('./data/Day07a') as f:
	global ttl
	ttl = {}
	for l in f:
		s = l.split(' ')
		a = s[1]
		b = s[7]
		d[b].append(a)
		orig.add(a)
		ttl[b] = delay(b)



	ready = orig - set(d.keys())
	for x in ready:
		ttl[x] = delay(x)
	print ready

	numVals = len(orig)
	step = 1
	while numVals > 0:
		ready = sorted(ready)
		nxt = getNext(ready)
		ready = set(ready)
		if nxt:
			res+= nxt
			l = d[nxt]
			for k,v in d.iteritems():
				if nxt in v: v.remove(nxt)
				if len(v) == 0 and not k in res: ready.add(k)

			numVals = 0
			for k,v in d.iteritems():
				numVals+= len(v)
		step+=1

	if len(ready) > 0:
		ready = sorted(ready)
		v = getNext(ready)
		while v:
			res+= v
			step+= 1
			v = getNext(ready)

	print "Part 1:", res
	print "Part2:", step

