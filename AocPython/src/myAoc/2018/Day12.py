'''
Created on Dec 12, 2018

@author: Mark
'''
state = "..#..#####.#.#.##....####..##.#.#.##.##.#####..####.#.##.....#..#.#.#...###..#..###.##.#..##.#.#.....#"
rules = {}

def transform(state):
	a=1

with open('./data/Day12') as f:
	for l in f:
		r = l.split(' => ')
		rules[r[0]] = r[1]
	
# 	for r, res in rules.iteritems():
# 		print r, res

for i in xrange(1, 21):
	state = transform(state)