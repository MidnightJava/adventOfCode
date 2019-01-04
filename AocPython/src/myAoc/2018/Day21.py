'''
Created on Jan 4, 2019

@author: maleone
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
		
'''
#ip 1
seti 123 0 4
bani 4 456 4
eqri 4 72 4
addr 4 1 1
seti 0 0 1
seti 0 1 4
bori 4 65536 3
seti 3730679 4 4
bani 3 255 5
addr 4 5 4
bani 4 16777215 4
muli 4 65899 4
bani 4 16777215 4
gtir 256 3 5
addr 5 1 1
addi 1 1 1
seti 27 1 1
seti 0 0 5
addi 5 1 2
muli 2 256 2
gtrr 2 3 2
addr 2 1 1
addi 1 1 1
seti 25 1 1
addi 5 1 5
seti 17 1 1
setr 5 2 3
seti 7 6 1
eqrr 4 0 5
addr 5 1 1
seti 5 1 1
'''

code = []
ip = 0
r0 = 0
reg = [r0,0,0,0,0,0]
ops = Ops()

with open('./data/Day21') as f:
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
	old_ip = ip
	old_reg = list(reg)
	Ops.__dict__[instr[0]](ops, reg, instr[1], instr[2], instr[3])
	print(old_ip, instr[0], old_reg, reg)
	ip = reg[ipreg] + 1
	
	
print('Part 1: %d' % r0)

