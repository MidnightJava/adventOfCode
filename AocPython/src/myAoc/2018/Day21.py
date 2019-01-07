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
# Part 1 answer determined by looking at reg values as the code runs.
# Program will exit when R0 == R4, so set R0 to value R4 will have
# when line 28 executes the first time
r0 = 16128384
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
	ip = reg[ipreg] + 1
	
	
print('Part 1: %d' % r0)

'''
For Part 2, we need the last unique value R4 will have when executing line 28
before a previous value repeats. So we emulate the program while short-circuiting
the loop that causes a large delay. We store R4 values at line 28. When we get a
value we've already seen, we print out the previous value and exit.
'''
s = set()
# Initialize registers
r3 = 65536
r4 = 3730679
r5 = 0

for i in range(3):
	# 8-12
	r5 = r3 & 255
	r4+= r5
	r4&= 16777215
	r4*= 65899
	r4&= 16777215
	
	'''
	Emulate the effects of looping over lines 18-25 until R2 == R3.
	R5 is the loop counter, and R2 increments by 256 each time. So
	when the loop exits, r5 will be set to the integer value of
	R3 / 256. R3 is set to R5 when the loop exits
	'''
	r3 = r5 = r3 / 256

# Line 28 executes here, but we don;t need to catch the first value
# Then lines 6-7 execute, followed by 8-12 again
r3 = r4 | 65536
r4 = 3730679

# 8-12
r5 = r3 & 255
r4+= r5
r4&= 16777215
r4*= 65899
r4&= 16777215

oldr4 = 0

# After the above sequence, the program follows a pattern that changes every other time through the loop
i = 0
done = False
while not done:
	#result of executing 18-25 until r2 = r3, incrementing r2 by 256 each iteration
	r3 = r5 = r3 / 256
	
	# lines 8-12
	r5 = r3 & 255
	r4+= r5
	r4&= 16777215
	r4*= 65899
	r4&= 16777215
	
	r5 = 0
	
	if i % 2 != 0:
		# Every other time we complete the loop, line
		# 28 executes, followed by lines 6-7, then 8-12.
		if r4 in s:
			print("Part 2:", oldr4)
			done = True
			break
		else:
			oldr4 = r4
			s.add(r4)
		
		# 6-7
		r3 = r4 | 65536
		r4 = 3730679
		
		# 8-12
		r5 = r3 & 255
		r4+= r5
		r4&= 16777215
		r4*= 65899
		r4&= 16777215
	
	i+= 1

# Part 1: 16128384
# Part 2: 7705368

