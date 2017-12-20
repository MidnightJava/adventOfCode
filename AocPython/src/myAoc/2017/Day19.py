'''
Created on Dec 19, 2017

@author: Mark
'''

grid = open("data/Day19").read().split('\n')

state = {'chars': [], 'count': 0}

def get_entry(grid):
	return (0, grid[0].index('|'))

def next_corner(cell, direc, state):
	row, col = cell
	if direc == 0: #right
		col+= 1
		state['count']+= 1
		while True:
			c = grid[row][col]
			if c == '|' or c == '-':
				col+= 1
				state['count']+= 1
			elif c.isalpha():
				col+=1
				state['chars'].append(c)
				state['count']+= 1
			elif c == '+':
				if row > 0 and grid[row-1][col] != ' ':
					return (row, col), 1 #go up
				elif row+1 < len(grid) and grid[row+1][col] != ' ':
					return (row, col), 3 # go down
			else:
				return None, direc
	elif direc == 2: #left
		col-= 1
		state['count']+= 1
		while True:
			c = grid[row][col]
			if c == '|' or c == '-':
				col-= 1
				state['count']+= 1
			elif c.isalpha():
				col-=1
				state['chars'].append(c)
				state['count']+= 1
			elif c == '+':
				if row > 0 and grid[row-1][col] != ' ':
					return (row, col), 1 #go up
				elif row+1 < len(grid) and grid[row+1][col] != ' ':
					return (row, col), 3 # go down
			else:
				return None, direc
	elif direc == 1: #up
		row-= 1
		state['count']+= 1
		while True:
			c = grid[row][col]
			if c == '|' or c == '-':
				row-= 1
				state['count']+= 1
			elif c.isalpha():
				row-=1
				state['chars'].append(c)
				state['count']+= 1
			elif c == '+':
				if col > 0 and grid[row][col-1] != ' ':
					return (row, col), 2 #go left
				elif col+1 < len(grid[row]) and grid[row][col+1] != ' ':
					return (row, col), 0 # go right
			else:
				return None, direc
	elif direc == 3: #down
		row+= 1
		state['count']+= 1
		while True:
			c = grid[row][col]
			if c == '|' or c == '-':
				row+= 1
				state['count']+= 1
			elif c.isalpha():
				row+=1
				state['chars'].append(c)
				state['count']+= 1
			elif c == '+':
				if col > 0 and grid[row][col-1] != ' ':
					return (row, col), 2 #go left
				elif col+1 < len(grid[row]) and grid[row][col+1] != ' ':
					return (row, col), 0 # go right
			else:
				return None, direc

def solve(cell, state):
	cell, direc = next_corner(cell, 3, state)
	while cell:
		cell, direc = next_corner(cell, direc, state)
	print "Part 1:", "".join(state['chars'])
	print "Part 2:", state['count']
	
solve(get_entry(grid), state)