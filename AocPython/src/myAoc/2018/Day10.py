'''
Created on Dec 10, 2018

@author: maleone
'''
from __future__ import print_function
import re

def print_grid():
	for y in xrange(top, bottom +1):
		for x in xrange(left, right +1):
			print('*' if is_point_at((x,y)) else ' ', end='')
		print('')

def is_point_at(loc):
	global points
	for pv in points:
		if pv[0] == loc: return True
	return False


def move():
	global left, right, top, bottom, points
	left, right, top, bottom = 100000, -100000, 100000, -100000
	newPoints = []
	for (p,v) in points:
		np = (p[0] + v[0], p[1] + v[1])
		newPoints.append((np,v))
		if np[0] > right: right = np[0]
		if np[0] < left: left = np[0]
		if np[1] > bottom: bottom = np[1]
		if np[1] < top: top = np[1]
	points = newPoints[:]

with open('./data/Day10') as f:
	pattern = 'position\=\<([-+]?\d+)\,([-+]?\d+)\>velocity\=\<([-+]?\d+)\,([-+]?\d+)\>'
	global points
	points = []
	left, right, top, bottom = 100000, -100000, 100000, -100000
	for l in f:
		m = re.search(pattern, l.strip().replace(' ', ''))
		if m:
			p = (int(m.group(1)), int(m.group(2)))
			v = (int(m.group(3)), int(m.group(4)))
			points.append((p,v))
			if p[0] > right: right = p[0]
			if p[0] < left: left = p[0]
			if p[1] > bottom: bottom = p[1]
			if p[1] < top: top = p[1]

	done = False
	i = 1
	while not done:
		x_range = right - left
		y_range = bottom - top
		prev_points = points
		move()
		if right - left > x_range or bottom - top > y_range:
			points = prev_points
			print('After %d moves' % (i-1))
			print_grid()
			done = True
		i+= 1

#Part 1: LRCXFXRP
#Part 2: 10630

