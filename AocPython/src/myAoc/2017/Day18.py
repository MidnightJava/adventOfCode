'''
Created on Dec 18, 2017

@author: maleone
'''
from _collections import defaultdict


d = defaultdict(int)
code = []
idx = 0

code = map(lambda x: x.strip(), open("data/Day18").readlines())
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
	

sent = 0
d = [defaultdict(int), defaultdict(int)]
sel = 0
waiting  = [False, False]
d[0]['p'] = 0
d[1]['p'] = 1
idx = [0,0]
q = [[], []]
inreg = ['', '']
while True:
	instr = code[idx[sel]]
	if waiting[sel] and len(q[(sel+1)%2]) > 0:
		reg = inreg[sel]
		val = q[(sel + 1) % 2].pop(0)
		d[sel][reg] = val
		waiting[sel] = False
		inreg[sel] = ''
		idx[sel]++ 1
		continue
	elif waiting[sel]:
		sel = (sel + 1) % 2
		continue
# 	if waiting[sel] and waiting[(sel + 1) % 2]:
# 		print "Part 2:", sent
# 		break
	print sent
	if "snd" in instr:
		reg = instr.split()[1]
		try:
			q[(sel + 1) % 2].append(int(reg))
		except ValueError:
			q[(sel + 1) % 2].append(d[sel][reg])
		if sel == 1:
			sent+= 1
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
			d[sel][reg]= d[sel][reg] % int(val)
		except ValueError:
			d[sel][reg]= d[sel][reg] % d[sel][val]
	elif 'rcv' in instr:
		parts = instr.split()
		reg = parts[1]
		if len(q[(sel + 1) % 2]) > 0:
			val = q[(sel + 1) % 2].pop(0)
			d[sel][reg] = val
# 			waiting[sel] = False
		else:
			waiting[sel] = True
			inreg[sel] = reg
# 			sel = (sel + 1) % 2
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
			idx[sel] = idx[sel] + offset
# 			sel = (sel + 1) % 2
			continue
	if sel == 0:
		print idx[sel], code[idx[sel]]
	else:
		print "\t\t", idx[sel], code[idx[sel]]
	idx[sel]+= 1
# 	sel = (sel + 1) % 2

	
#16001 too high
