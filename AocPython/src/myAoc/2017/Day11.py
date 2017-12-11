'''
Created on Dec 11, 2017

@author: Mark
'''
x = 0
y = 0
z = 0
steps = []
f = open("data/Day11")
grids = f.read().strip().split(',')
for grid in grids:
		if 'n' == grid:
			y+= 1
		elif 's' == grid:
			y-= 1
		elif 'ne' == grid:
			x+= 1
		elif 'se' == grid:
			x+= 1
			y-= 1
		elif 'sw' == grid:
			x-= 1
		elif 'nw' == grid:
			x-= 1
			y+= 1
		steps.append((abs(x) + abs(y) + abs(x+y))/2)
#
print "Part 1:", (abs(x) + abs(y) + abs(x+y))/2
print "Part 2:", max(steps)

		#1042 too high  not 747, 748, 825
		#try 412, 584, 824

		#Part 2:
		#3095 too high 1547 too low