'''
Created on Dec 22, 2017

@author: maleone
'''
from _collections import defaultdict


grid = defaultdict(int)
lines = open("data/Day22").read().strip().split()
width = len(lines[0])
for i in xrange(len(lines)) :
	for j in xrange(width):
		if lines[i][j] == '#':
			grid[(-i,j)] = 1
		else:
			grid[(-i,j)] = 0
loc = (-(len(lines) / 2), width / 2)

count = 0
d = 1 #up
for i in xrange(10000):
	if grid[loc] == 1:
		d = (d + 3) % 4 # right turn
	else:
		d = (d + 5) % 4 #left turn
	grid[loc] = 1 - grid[loc] # toggle 1/0
	if grid[loc] == 1:
		count+= 1
	if d ==0:
		loc = (loc[0], loc[1] + 1)
	elif d == 1:
		loc = (loc[0] + 1, loc[1])
	elif d == 2:
		loc = (loc[0], loc[1] - 1)
	elif d == 3:
		loc = (loc[0] - 1, loc[1])

print "Part 1:", count

grid = defaultdict(int)
lines = open("data/Day22").read().strip().split()
width = len(lines[0])
#state 0: cleaned, 1: weakened, 2: infected, 3: flagged
for i in xrange(len(lines)) :
	for j in xrange(width):
		if lines[i][j] == '#':
			grid[(-i,j)] = 2
		else:
			grid[(-i,j)] = 0
loc = (-(len(lines) / 2), width / 2)



count = 0
d = 1 #up
for i in xrange(10000000):
	if grid[loc] == 0:
		d = (d + 5) % 4 # left turn
	elif grid[loc] == 2:
		d = (d + 3) % 4 # right turn
	elif grid[loc] == 3:
		d = (d + 2) % 4 # reverse
	grid[loc] = state = (grid[loc] + 1) % 4
	if state == 2: count+= 1
	if d ==0:
		loc = (loc[0], loc[1] + 1)
	elif d == 1:
		loc = (loc[0] + 1, loc[1])
	elif d == 2:
		loc = (loc[0], loc[1] - 1)
	elif d == 3:
		loc = (loc[0] - 1, loc[1])

print "Part 2:", count

