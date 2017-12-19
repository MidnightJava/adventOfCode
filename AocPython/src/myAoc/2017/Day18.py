'''
Created on Dec 18, 2017

@author: maleone
'''
from _collections import defaultdict


d = defaultdict(int)
code = map(lambda x: x.strip(), open("data/Day18").readlines())
idx = 0

while idx >= 0 and idx < len(code):
	instr = code[idx]
	if "snd" in instr:
		val = instr.split()[1]
		play = d[val]
	elif 'set' in instr:
		parts = instr.split()
		reg, val = parts[1], parts[2]
		try:
			d[reg] = int(val)
		except ValueError:
			d[reg] = d[val]
	elif 'add' in instr:
		parts = instr.split()
		reg, val = parts[1], parts[2]
		try:
			d[reg]+= int(val)
		except ValueError:
			d[reg]+= d[val]
	elif 'mul' in instr:
		parts = instr.split()
		reg, val = parts[1], parts[2]
		try:
			d[reg]*= int(val)
		except ValueError:
			d[reg]*= d[val]
	elif 'mod' in instr:
		parts = instr.split()
		reg, val = parts[1], parts[2]
		try:
			d[reg]= d[reg] % int(val)
		except ValueError:
			d[reg]= d[reg] % d[val]
	elif 'rcv' in instr:
		parts = instr.split()
		val = parts[1]
		if val:
			print "Part 1:", play
			break
	elif 'jgz' in instr:
		parts = instr.split()
		val = parts[1]
		offset = parts[2]
		if d[val]:
			try:
				idx = idx + int(offset)
			except ValueError:
				idx = idx + d[offset]
			continue
	idx+= 1


sent = [0, 0]
d = [defaultdict(int), defaultdict(int)]
sel = 0
waiting  = [False, False]
d[1]['p'] = 1
idx = [0,0]
q = [[], []]
inreg = ['', '']
while True:
	if idx[sel] <0 or idx[sel] > len(code):
		#Doesn't happen, so no need to set waitign state accordingly
		print "Index out of range"
		break
	instr = code[idx[sel]]
	if "snd" in instr:
		sent[sel]+= 1
		reg = instr.split()[1]
		try:
			q[sel].append(int(reg))
		except ValueError:
			q[sel].append(d[sel][reg])
	elif 'set' in instr:
		parts = instr.split()
		reg, val = parts[1], parts[2]
		try:
			d[sel][reg] = int(val)
		except ValueError:
			d[sel][reg] = d[sel][val]
	elif 'add' in instr:
		parts = instr.split()
		reg, val = parts[1], parts[2]
		try:
			d[sel][reg]+= int(val)
		except ValueError:
			d[sel][reg]+= d[sel][val]
	elif 'mul' in instr:
		parts = instr.split()
		reg, val = parts[1], parts[2]
		try:
			d[sel][reg]*= int(val)
		except ValueError:
			d[sel][reg]*= d[sel][val]
	elif 'mod' in instr:
		parts = instr.split()
		reg, val = parts[1], parts[2]
		try:
			d[sel][reg]%= int(val)
		except ValueError:
			d[sel][reg]= d[sel][reg] % d[sel][val]
	elif 'rcv' in instr:
		parts = instr.split()
		reg = parts[1]
		if len(q[(sel + 1) % 2]) > 0:
			val = q[(sel + 1) % 2].pop(0)
			d[sel][reg] = val
			waiting[sel] = False
		else:
			if len(q[sel]) == 0 and waiting[(sel + 1) % 2]:
				print "Part2:", sent[1]
				break
			waiting[sel] = True
			inreg[sel] = reg
			sel = (sel + 1) % 2
			continue
	elif 'jgz' in instr:
		parts = instr.split()
		try:
			val = int(parts[1])
		except ValueError:
			val = int(d[sel][parts[1]])
		try:
			offset = int(parts[2])
		except ValueError:
			offset = int(d[sel][parts[2]])
		if val > 0:
			idx[sel]+= offset
			continue
	idx[sel]+= 1
