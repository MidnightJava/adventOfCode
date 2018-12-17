'''
Created on Dec 16, 2018

@author: Mark
'''

from collections import defaultdict

class Ops:
	
	def addr(self, before, after, a, b, c):
		res = list(before)
		res[c] = before[a] + before[b]
		return res
		
	def addi(self, before, after, a, b, c):
		res = list(before)
		res[c] = before[a] + b
		return res
	
	def mulr(self, before, after, a, b, c):
		res = list(before)
		res[c] = before[a] * before[b]
		return res
		
	def muli(self, before, after, a, b, c):
		res = list(before)
		res[c] = before[a] * b
		return res
	
	def banr(self, before, after, a, b, c):
		res = list(before)
		res[c] = before[a] & before[b]
		return res
		
	def bani(self, before, after, a, b, c):
		res = list(before)
		res[c] = before[a] & b
		return res
		
	def borr(self, before, after, a, b, c):
		res = list(before)
		res[c] = before[a] | before[b]
		return res
		
	def bori(self, before, after, a, b, c):
		res = list(before)
		res[c] = before[a] | b
		return res
		
	def setr(self, before, after, a, b, c):
		res = list(before)
		res[c] = before[a]
		return res
		
	def seti(self, before, after, a, b, c):
		res = list(before)
		res[c] = a
		return res
		
	def gtir(self, before, after, a, b, c):
		res = list(before)
		res[c] = 1 if a > before[b] else 0
		return res
		
	def gtri(self, before, after, a, b, c):
		res = list(before)
		res[c] = 1 if before[a] > b else 0
		return res
		
	def gtrr(self, before, after, a, b, c):
		res = list(before)
		res[c] = 1 if before[a] > before[b] else 0
		return res
		
	def eqir(self, before, after, a, b, c):
		res = list(before)
		res[c] = 1 if a == before[b] else 0
		return res
		
	def eqri(self, before, after, a, b, c):
		res = list(before)
		res[c] = 1 if before[a] == b else 0
		return res
		
	def eqrr(self, before, after, a, b, c):
		res = list(before)
		res[c] = 1 if before[a] == before[b] else 0
		return res
		
with open('./data/Day16') as f:
	lines = []
	samples = []
	code = []
	for l in f:
		if not len(l.strip()): continue
		lines.append(l)
	i = 0
	scount = 0
	while i < len(lines):
		if lines[i].startswith('Before'):
			scount+= 1
			before = eval(lines[i].replace('Before: ', ''))
			op = map(int, lines[i+1].split())
			after = eval(lines[i+2].replace('After: ', ''))
			samples.append((op, before, after))
			i+= 3
		else:
			code.append(map(int, lines[i].split()))
			i+= 1
	
	total = 0
	ops = Ops()
	results = defaultdict(set)
	for s in samples:
		count = 0
		op = s[0]
		before = s[1]
		after = s[2]
		methods = set()
		for name, method in Ops.__dict__.iteritems():
			if callable(method):
				if method(ops, before, after, op[1], op[2], op[3]) == after:
					count+= 1
					methods.add(name)
		if count >= 3: total+= 1
		for method in methods:
			results[op[0]].add(method)

	print "Part 1:", total
	
	done = False
	op_map = {}
	while not done:
		found = False
		for k,v in results.items():
			if len(v) == 1:
				found = True
				m = op_map[k] = v.pop()
				del results[k]
				for k2, v2 in results.items():
					if m in v2:
						v2.remove(m)
		if not found: done = True
	
	inp = [0,0,0,0]
	for c in code:
		m = op_map[c[0]]
		inp = Ops.__dict__[m](ops, inp, inp, c[1], c[2], c[3])
		
		
	print "Part 2:", inp[0]

# Part 1: 640
# Part 2: 472
	
			