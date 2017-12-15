'''
Created on Dec 14, 2017

@author: Mark
'''
from __future__ import print_function
from collections import Counter
from _collections import defaultdict


inp_str = 'stpzcrnm'
# inp_str = 'flqrgnkx' #test data
suffix = [17, 31, 73, 47, 23]
grid = {}
groups = defaultdict(set)

size = 256
def getInput(inp):
	inp2 = map(lambda x: ord(x), inp)
	inp2.extend(suffix)
	return inp2

def solve(lst, idx, skip, inp):
	inp = getInput(inp)
	for l in inp:
		if l == 0:
			idx = (idx + skip) % size
			skip+= 1
			continue
		sublist = []
		for i in xrange(l):
			sublist.append(lst[(idx + i) % size])
		sublist = sublist[::-1]
		for i in xrange(l):
			lst[(idx +i) % size] = sublist[i]
		idx = (idx + skip + l) % size
		skip+=1
	return idx, skip

count = 0
for i in xrange(128):
	idx = skip = 0
	lst = list(xrange(size))
	for x in xrange(64):
		idx, skip = solve(lst, idx, skip, inp_str + '-' + str(i))
	lst2 = []
	val = 0
	for i2 in xrange(size):
		val^= lst[i2]
		if (i2 + 1) % 16 == 0:
			lst2.append(val)
			val = 0

	out =''
	for v in lst2:
		hval = hex(v)[2:]
		if len(hval) == 1:
			hval = '0' + hval
		out+= hval
	bin_str = bin(int(out, 16))[2:].zfill(4)
	for _ in range(128 - len(bin_str)):
		bin_str = '0' + bin_str
	counter = Counter(bin_str)
	count+= counter['1']
	line = map(lambda x: '.' if x == '0' else '#', bin_str)
	for j in xrange(128):
		grid[(i,j)] = line[j]

print("Part 1: {}".format(count))

def next_cell():
	global grid
	for i in xrange(128):
		for j in xrange(128):
			if grid[(i,j)] == '#':
				return (i,j)
	
def get_nbrs(cell):
	nbrs = []
	for x in [1, -1]:
		i = cell[0] + x
		if i >= 0 and i <= 127 and grid[(i, cell[1])] == '#':
			nbrs.append((i, cell[1]))
	for y in [1, -1]:
		j = cell[1] + y
		if j >= 0 and j <= 127 and grid[(cell[0], j)] == '#':
			nbrs.append((cell[0], j))
	return nbrs
			
def visit(cell, grp):
	global grid
	i,j = cell
	grid[(i,j)] = grp
	groups[grp].add((i,j))
	for n in get_nbrs(cell):
		visit(n, grp)

grp = 0
def next_grp():
	global grp
	grp+= 1
	return grp
	
cell = next_cell()
while cell:
	visit(cell, next_grp())
	cell = next_cell()

print ("Part 2:", grp)
