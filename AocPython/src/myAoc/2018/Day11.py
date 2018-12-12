'''
Created on Dec 10, 2018

@author: Mark
'''

import time

serial_no = 2187

grid = {}
scores = {}

def get_pwr(x, y):
	n = ((x + 10) * y + serial_no) * (x+10)
	n_str = str(n)
	if len(n_str) < 3: return -5
	return (int(n_str)/100 % 10) -5

def make_grid():
	global grid
	for y in xrange(1, 301):
		for x in xrange(1, 301):
			grid[(x,y)] = get_pwr(x, y)

def solve(n):
	global scores
	for y in xrange(1, 301-n):
		for x in xrange(1, 301-n):
			pwr = 0
			if not ((x,y), n) in scores:
				for y2 in xrange(n):
					for x2 in xrange(n):
						pwr+= grid[(x+x2, y+y2)]
				scores[((x,y), n)] = pwr

	max_score = 0
	winner = None
	for k,v in scores.iteritems():
		if v > max_score:
			max_score = v
			winner = k
	return winner, max_score

make_grid()

start_time = time.time()
print "Part 1:", solve(3)

max_score = 0
winner = None
no_incr_count = 0
for n in xrange(1, 50):
	if no_incr_count == 3:
		break
	print "trying size", n
	w, sc = solve(n)
	if sc > max_score:
		no_incr_count = 0
		max_score = sc
		winner = w
	else:
		no_incr_count+= 1

print "Part 2:", winner
print "time:", time.time() - start_time
