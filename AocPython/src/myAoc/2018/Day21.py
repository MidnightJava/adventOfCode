'''
Created on Jan 4, 2019

@author: maleone
'''
from __future__ import print_function
from __builtin__ import True

class Ops:

	def addr(self, reg, a, b, c):
		reg[c] = reg[a] + reg[b]

	def addi(self, reg, a, b, c):
		reg[c] = reg[a] + b

	def mulr(self, reg, a, b, c):
		reg[c] = reg[a] * reg[b]

	def muli(self, reg, a, b, c):
		reg[c] = reg[a] * b

	def banr(self, reg, a, b, c):
		reg[c] = reg[a] & reg[b]

	def bani(self, reg, a, b, c):
		reg[c] = reg[a] & b

	def borr(self, reg, a, b, c):
		reg[c] = reg[a] | reg[b]

	def bori(self, reg, a, b, c):
		reg[c] = reg[a] | b

	def setr(self, reg, a, b, c):
		reg[c] = reg[a]

	def seti(self, reg, a, b, c):
		reg[c] = a

	def gtir(self, reg, a, b, c):
		reg[c] = 1 if a > reg[b] else 0

	def gtri(self, reg, a, b, c):
		reg[c] = 1 if reg[a] > b else 0

	def gtrr(self, reg, a, b, c):
		reg[c] = 1 if reg[a] > reg[b] else 0

	def eqir(self, reg, a, b, c):
		reg[c] = 1 if a == reg[b] else 0

	def eqri(self, reg, a, b, c):
		reg[c] = 1 if reg[a] == b else 0

	def eqrr(self, reg, a, b, c):
		reg[c] = 1 if reg[a] == reg[b] else 0

code = []
ip = 0
reg = [0,0,0,0,0,0]
ops = Ops()

with open('./data/Day21') as f:
	for l in f:
		if l.startswith('#ip'):
			ipreg = int(l.split()[1])
		else:
			instr = l.split()
			instr = map(lambda x: int(x) if x.isdigit() else x, instr)
			code.append(instr)

s = set()
prev_r4 = 0
p1_found = False
while ip < len(code):
	instr = code[ip]
	reg[ipreg] = ip
	old_ip = ip
	old_reg = list(reg)
	if ip == 28:
		# Line 28 is the only one depending on reg 0. The program exits here
		# if reg 0 == reg 4
		if not p1_found: print("Part 1:", reg[4])
		p1_found = True
		reg[1] = 5
		if reg[4] in s:
			# The last unique value in r4 at line 28 (before they start repeating) is the answer
			print("Part 2", prev_r4)
			break
		prev_r4 = reg[4]
		s.add(reg[4])
	elif ip == 18:
		reg[5] = reg[3] /256
		reg[3] = reg[5]
		reg[ipreg] = 25
	else:
		Ops.__dict__[instr[0]](ops, reg, instr[1], instr[2], instr[3])
	ip = reg[ipreg] + 1

# Part 1: 16128384
# Part 2: 7705368

