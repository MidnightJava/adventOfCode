'''
Created on Dec 12, 2018

@author: Mark
'''
from __future__ import print_function

rules = {}

def transform(inp):
	res = ''
	i = 0
	last = inp.rindex('#')
	while i <= last + 1:
		if i == last or i == last + 1:
			p = inp[i-2:i+1] + '..'
		else:
			p = inp[i-2:i+3]
		res+= rules[p] if p in rules else '.'
		i+= 1
	return res + '.'

with open('./data/Day12') as f:
	for l in f:
		r = l.strip().split(' => ')
		rules[r[0]] = r[1]

pad = 40
state = '.' * pad + "#..#####.#.#.##....####..##.#.#.##.##.#####..####.#.##.....#..#.#.#...###..#..###.##.#..##.#.#.....#" + '.' * pad
for i in xrange(20):
	state = transform(state)

print('Part 1:', sum([i - pad for i in xrange(len(state)) if state[i] == '#']))

# Part 1: 1447
# Part 2: 480 + 50e9*2100/100 = 1050000000480