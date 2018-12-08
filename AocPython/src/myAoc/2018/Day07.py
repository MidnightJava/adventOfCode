'''
Created on Dec 7, 2018

@author: maleone
'''

from collections import defaultdict

class Worker:
	
	def __init__(self):
		self.idle = True
		self.task = None

	def start(self, task):
		self.task = task
		self.idle = False
		self.ttl = delay(task)
		
	def stop(self):
		self.idle = True
	
	def tick(self):
		if hasattr(self,'ttl'):
			self.ttl = max(self.ttl -1, 0)
		
	def ready(self):
		if hasattr(self, 'ttl'):
			return self.ttl == 0 and not self.idle
		return False

def working(task):
	global workers
	for w in workers:
		if task == w.task: return True
	return False

def getNext(ready):
	if part1:
		nxt = ready.pop(0) if len(ready) else None
	else:
		for worker in workers:
			if ready:
				if worker.idle:
					worker.start(ready.pop(0))
		for w in workers: w.tick()
		candidates = [w for w in workers if w.ready()]
		candidates = sorted(candidates, key=lambda x: x.task)
		if candidates:
			w = candidates.pop(0)
			nxt = w.task
			w.stop()
		else:
			nxt = None
	return nxt

def delay(c):
	return ord(c) - 4

for part1 in [True, False]:
	d = defaultdict(list)
	orig = set()
	ready = set()
	res = ''
	with open('./data/Day07') as f:
		for l in f:
			s = l.split(' ')
			a = s[1]
			b = s[7]
			d[b].append(a)
			orig.add(a)
	
		ready = orig - set(d.keys())
		numVals = len(orig)
		step = 0
		global workers
		workers = [Worker(), Worker(), Worker(), Worker(), Worker()]
		while numVals > 0 or ready:
			ready = sorted(ready)
			nxt = getNext(ready)
			ready = set(ready)
			if nxt:
				res+= nxt
				l = d[nxt]
				for k,v in d.iteritems():
					if nxt in v: v.remove(nxt)
					if len(v) == 0 and not k in res and not working(k): ready.add(k)
	
				numVals = 0
				for k,v in d.iteritems():
					numVals+= len(v)
			step+=1
	
		if part1:
			print "Part 1:", res
		else:
			for w in workers:
				step+= w.ttl
			print "Part 2:", step

#Part 1: BHRTWCYSELPUVZAOIJKGMFQDXN
#Part 2: 959