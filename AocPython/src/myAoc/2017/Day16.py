'''
Created on Dec 15, 2017

@author: Mark
'''
import re

line = list('abcdefghijklmnop')
l = open("data/Day16").read().strip()

loop = 1
done = False
mod = 1
while not done:
	for mv in l.split(','):
		if 'x' in mv:
			a, b = map(lambda x: int(x), mv[1:].split('/'));
			line[a], line[b] = line[b], line[a]
		elif 'p' in mv:
			a, b = map(lambda x: line.index(x), mv[1:].split('/'));
			line[a], line[b] = line[b], line[a]
		else:
			m = re.match('s(\d+)', mv)
			n = int(m.group(1))
			line = line[-n:] + line[:(16 - n)]
	out = "".join(line)
	if loop == 1:
		print "Part 1:", out
		seen = out
	elif out == seen and mod == 1:
		#pattern repeats at this interval
		interval = loop - 1
		mod = (1000000000 % interval) + interval
	if mod > 1 and loop % mod == 0:
		print "Part 2:", out
		done = True
	loop+= 1
			