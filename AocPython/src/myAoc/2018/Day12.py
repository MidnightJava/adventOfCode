'''
Created on Dec 12, 2018

@author: Mark
'''
from __future__ import print_function

rules = {}

def transform(inp):
	pad = 0
	res = ''
	i = 0
	first = inp.index('#')
	last = inp.rindex('#')
	while i <= last +1:
		if i == 0:
			p = '..' + inp[i:i+3]
		elif i == 1:
			p = '.' + inp[i-1:i+3]
		elif i == len(inp) - 2:
			p = inp[i-2:] + '.'
		elif i == len(inp) - 1:
			p = inp[i-2:] + '..'
		elif i == last:
			p = inp[i-2:i+1] + '..'
		elif i == last + 1:
			p = inp[i-3:i] + '.'
		else:
			p = inp[i-2:i+3]
		if p in rules:
			if rules[p].strip() == '#' and i <= first:
				pad+= 1
			res+= rules[p].strip()
		else:
			res+= '.'
		i+= 1
	return res

with open('./data/Day12') as f:
	for l in f:
		r = l.split(' => ')
		rules[r[0].strip()] = r[1].strip()

# 	for r, res in rules.iteritems():
# 		print(r, res)

state = ('.'*40) + "#..#####.#.#.##....####..##.#.#.##.##.#####..####.#.##.....#..#.#.#...###..#..###.##.#..##.#.#.....#" + ('.'*40)
# state = ('.'*40) + '#..#.#..##......###...###' + ('.' * 40)
for i in xrange(20):
	print(i, state)
	state = transform(state)

off = 40
tot = 0
i = 0
for c in state:
	if c == '#':
		tot+= (i - off)
	i+= 1
print('Part 1:', state, tot)

# 2,6,9,12,16,19# Part 1: 106 too low 1467 too high not 1411
