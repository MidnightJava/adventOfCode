'''
Created on Dec 13, 2018

@author: maleone
'''
from __future__ import print_function

part1 = True

def grid(x,y):
	return _grid[y][x]

def setGrid(x, y, c):
	grid(x,y).c = c

class Cell:
	def __init__(self, c, loc):
		global cars
		if c in ['<','>','^','v']:
			self.car = c
			self.track = None
			self.turn = 0
			cars+= 1
		else:
			self.car = None
			self.track = c
		self.loc = loc
		self.turn_loookup = [
			{'<': 'v', 'v': '>', '>': '^','^': '<'}, # left
			{'<': '<', '>': '>', '^': '^', 'v': 'v'}, # straight
			{'<': '^', 'v': '<', '>': 'v', '^': '>'} # right
		]

	def move(self, moved):
		global cars
# 		print('car %s at %s' % (self.car, self.loc))
		if self.car is None:
			print("Trying to move a track cell!")
			return False
		self.track = self.getTrack()
		if self.car == '<':
			loc_delta = (-1, 0)
		elif self.car == '>':
			loc_delta = (1, 0)
		elif self.car == '^':
			loc_delta = (0, -1)
		elif self.car == 'v':
			loc_delta = (0, 1)
		else:
			print('invalid car', self.car)

		newLoc = (self.loc[0] + loc_delta[0], self.loc[1] + loc_delta[1])
		nextCell = grid(newLoc[0], newLoc[1])
# 		print('moving to %s with value %s' % (newLoc, nextCell.car or nextCell.track))
		if nextCell.car:
			if part1:
				print('Part 1:', newLoc)
				return False
			else:
				self.car = None
				nextCell.car = None
				cars-= 2
				if cars == 1:
					return False
		if self.car:		
			nextCell.placeCar(self.car, self.turn)
			self.car = None
		moved.add(newLoc)
		return True

	def getTrack(self):
		if self.track: return self.track
		if self.car == 'v' or self.car == '^':
			return '|'
		if self.car == '<' or self.car == '>':
			return '-'
		else:
			print("Invalid car %s while getting track" % self.car)

	def makeTurn(self):
		self.car = self.turn_loookup[self.turn][self.car]
		self.turn = (self.turn + 1) % 3

	def placeCar(self, car, turn):
		self.turn = turn
		if self.track == '|' or self.track == '-':
			self.car = car
		elif self.track == '+':
			self.car = car
			self.makeTurn()
		elif self.track == '\\':
			if car == '^': self.car = '<'
			elif car == 'v': self.car = '>'
			elif car == '<': self.car = '^'
			elif car == '>': self.car = 'v'
			else: print('unexpected car value %s for curve %s' % (self.car, self.track))
		elif self.track == '/':
			if car == '^': self.car = '>'
			elif car == 'v': self.car = '<'
			elif car == '<': self.car = 'v'
			elif car == '>': self.car = '^'
			else: print('unexpected car value %s for curve %s' % (self.car, self.track))
		else:
			print('unhandled track in placeCar. Track: %s  car: %s' % (self.track, car))
# 		print('placed car %s at %s' % (self.car, self.loc))

with open('./data/Day13') as f:
	global _grid
	global cars
	cars = 0
	_grid = []
	y = 0
	for line in f:
		x = 0
		_grid.append([])
		for c in line:
			_grid[-1].append(Cell(c, (x,y)))
			x+= 1
		y+= 1

def findLastCar():
	for y in _grid:
		for x in y:
			if x.car is not None:
				return x.loc

def tick():
	moved = set()
	lastCar = False
	for y in _grid:
		for x in y:
			if x.car is not None:
				if not (x.loc) in moved:
					if not x.move(moved):
						if part1:
							return False
						else:
							lastCar = True
	if lastCar:
		print('Part2:', findLastCar())
		return False

	return True

cont = True
while cont:
	cont = tick()


# Part1: 83,106
# Part2 132,26
