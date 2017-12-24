'''
Created on Dec 22, 2017

@author: Mark
'''
code = []
d = {k:0 for k in 'abcdefgh'}
part2 = True
p2 = 'opt' if part2 else ''
# p2 = ''
with open("data/Day23"+ p2) as f:
	for line in f:
		if '#' not in line:
			code.append(line.strip())

if part2:
	d['a'] = 1

idx = 0
count = 0
fcount  =0
while idx < len(code):
	instr = code[idx]
	if 'set' in instr:
		parts = instr.split()
		reg, val = parts[1], parts[2]
		try:
			if part2 and reg == 'f':
				if fcount % 11 == 0:
					d[reg] = 1
				else:
					d[reg] = 0
				fcount += 1
			else:
				d[reg] = int(val)
		except ValueError:
			d[reg] = d[val]
	elif 'sub' in instr:
		parts = instr.split()
		reg, val = parts[1], parts[2]
		try:
			d[reg]-= int(val)
		except ValueError:
			d[reg]-= d[val]
	elif 'mul' in instr:
		parts = instr.split()
		reg, val = parts[1], parts[2]
		try:
			d[reg]*= int(val)
		except ValueError:
			d[reg]*= d[val]
		count+= 1
	elif 'jnz' in instr:
		parts = instr.split()
		try:
			val = int(parts[1])
		except ValueError:
			val = int(d[parts[1]])
		try:
			offset = int(parts[2])
		except ValueError:
			offset = int(d[parts[2]])
		if val != 0:
			idx+= offset
			continue
	else:
		print "Unknown instruction", instr
	idx+= 1

if part2:
	print "Part 2:", d['h'] - 1
else:
	print "Part 1:", count
#Part 2: 1000 too high