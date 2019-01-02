'''
Created on Jan 1, 2019

@author: Mark
'''
from __future__ import print_function

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

with open('./data/Day19') as f:
	for l in f:
		if l.startswith('#ip'):
			ipreg = int(l.split()[1])
		else:
			instr = l.split()
			instr = map(lambda x: int(x) if x.isdigit() else x, instr)
			code.append(instr)

while ip < len(code):
	instr = code[ip]
	reg[ipreg] = ip
	Ops.__dict__[instr[0]](ops, reg, instr[1], instr[2], instr[3])
	ip = reg[ipreg] + 1
print('Part 1: %d' % reg[0])

reg = [1,0,0,0,0,0]
# value of reg 4 after running lines 0 and 17-35, then returning to line 1
limit = 10551394
reg0 = 0
reg3 = 0
# Line 1 initializes reg 3 to 1
# Line 2 initializes reg1 to 1
# Loop through lines 3-11, incrementing reg 1 each time, until reg1 == limit.
# When this loop completes, incr reg3 by one, then return to line 2, reset the loop counter (reg1), and loop through lines 3-11 again
# Whenever reg3 * loop counter == limit, incr reg0 by value of reg3
# Exit outer loop when reg3 == limit
while reg3 <= limit:
	if reg3 != 0 and limit % reg3 == 0: reg0+= reg3
	reg3 += 1
print('Part 2:', reg0)

# Part 1: 1728
# Part 2: 18200448

