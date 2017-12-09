'''
Created on Dec 9, 2017

@author: Mark
'''

score = 0
stack = []
lastScore = 0
garbage = False
gcount = 0


with open("data/Day09") as f:
	for line in f:
		i = 0
		while i < len(line):
			if garbage:
				if line[i] == '>':
					garbage = False
				elif line[i] == '!':
					i += 1
				else:
					gcount += 1
				i += 1
				continue
			if line[i] == '{':
				lastScore += 1
				stack.append(lastScore)
			elif line[i] == '}':
				lastScore -= 1
				score += stack.pop()
			elif line[i] == '!':
				i += 1
			elif line[i] == '<':
				garbage = True
			i += 1
	print "Part 1", score
	print "Part 2", gcount
			
			
