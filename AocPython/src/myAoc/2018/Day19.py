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

part1 = False
code = []
ip = 0
reg = [0 if part1 else 1,0,0,0,0,0]
ops = Ops()

# with open('./data/Day19') as f:
# 	for l in f:
# 		if l.startswith('#ip'):
# 			ipreg = int(l.split()[1])
# 		else:
# 			instr = l.split()
# 			instr = map(lambda x: int(x) if x.isdigit() else x, instr)
# 			code.append(instr)
# 
# while ip < len(code):
# 	instr = code[ip]
# 	reg[ipreg] = ip
# 	old_ip = ip
# 	Ops.__dict__[instr[0]](ops, reg, instr[1], instr[2], instr[3])
# 	ip = reg[ipreg] + 1
# # 	if instr == ['addr', 3, 0, 0]:
# # 		print(instr, reg)
# 	print(old_ip, reg)
# print(reg)
# print(ipreg)
# for c in code:
# 	print(c)
# reg0 = 0
# reg3 = 0
# count = 0
# while reg3 <= 10551394:
# 	if count % 10551394 == 0:
# 		reg3 += 3
# 		print('Reg 3: %d Reg 0: %d' % (reg3, reg0))
# 	if (count * reg3) % 10551394 == 0:
# 		reg0 += reg3
# 	count = (count + 1)
# print(reg0)

limit = 10551394
reg0 = 0
reg3 = 0
count = 0
while reg3 <= limit:
	reg3 += 3
	if (count * reg3) % limit == 0:
		reg0 += reg3
	count += 1
print(reg0)
		


# Part 1:
# Part 2: 31654179 too high 10551395 too low not 2701156864 or 2701157120 or 42205576 not 32222829