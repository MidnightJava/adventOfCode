'''
Created on Dec 16, 2018

@author: Mark
'''

from collections import defaultdict

class Ops:
	
	def addr(self, before, a, b, c):
		before[c] = before[a] + before[b]
		return before
		
	def addi(self, before, a, b, c):
		before[c] = before[a] + b
		return before
	
	def mulr(self, before, a, b, c):
		before[c] = before[a] * before[b]
		return before
		
	def muli(self, before, a, b, c):
		before[c] = before[a] * b
		return before
	
	def banr(self, before, a, b, c):
		before[c] = before[a] & before[b]
		return before
		
	def bani(self, before, a, b, c):
		before[c] = before[a] & b
		return before
		
	def borr(self, before, a, b, c):
		before[c] = before[a] | before[b]
		return before
		
	def bori(self, before, a, b, c):
		before[c] = before[a] | b
		return before
		
	def setr(self, before, a, b, c):
		before[c] = before[a]
		return before
		
	def seti(self, before, a, b, c):
		before[c] = a
		return before
		
	def gtir(self, before, a, b, c):
		before[c] = 1 if a > before[b] else 0
		return before
		
	def gtri(self, before, a, b, c):
		before[c] = 1 if before[a] > b else 0
		return before
		
	def gtrr(self, before, a, b, c):
		before[c] = 1 if before[a] > before[b] else 0
		return before
		
	def eqir(self, before, a, b, c):
		before[c] = 1 if a == before[b] else 0
		return before
		
	def eqri(self, before, a, b, c):
		before[c] = 1 if before[a] == b else 0
		return before
		
	def eqrr(self, before, a, b, c):
		before[c] = 1 if before[a] == before[b] else 0
		return before
		
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
	all_matches = defaultdict(set)
	for s in samples:
		count = 0
		op = s[0]
		before = s[1]
		after = s[2]
		methods = set()
		for name, method in Ops.__dict__.iteritems():
			if callable(method):
				if method(ops, list(before), op[1], op[2], op[3]) == after:
					count+= 1
					methods.add(name)
		if count >= 3: total+= 1
		for method in methods:
			all_matches[op[0]].add(method)

	print "Part 1:", total
	
	done = False
	op_map = {}
	# Iteratively find op codes that have only one match to a method.
	# Assign that method to the op code, remove instances of that
	# method in all other op code matches, and remove it from the all_matches
	# map. Iterate until no more single matches are found
	while not done:
		found = False
		for k,v in all_matches.items():
			if len(v) == 1:
				found = True
				m = op_map[k] = v.pop()
				del all_matches[k]
				for k2, v2 in all_matches.items():
					if m in v2:
						v2.remove(m)
		if not found: done = True
	
	inp = [0,0,0,0]
	for c in code:
		m = op_map[c[0]]
		inp = Ops.__dict__[m](ops, inp, c[1], c[2], c[3])
		
		
	print "Part 2:", inp[0]

# Part 1: 640
# Part 2: 472
	
			