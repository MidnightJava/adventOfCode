'''
Created on Dec 14, 2017

@author: Mark
'''
from __future__ import print_function
from collections import Counter


inp_str = 'stpzcrnm'
inp_str = 'flqrgnkx'
suffix = [17, 31, 73, 47, 23]
grid = {}

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
# 	print out
	bin_str = bin(int(out, 16))[2:].zfill(4)
	for _ in range(128 - len(bin_str)):
		bin_str = '0' + bin_str
# 	print bin_str
	counter = Counter(bin_str)
	count+= counter['1']
	line = map(lambda x: '.' if x == '0' else '#', bin_str)
	for j in xrange(128):
		grid[(i,j)] = line[j]
# 	print "".join(line)

print("Part 1:", count)

grp = 0
def next_grp():
	global grp
	grp+= 1
	return grp

regions  = set()
for i in xrange(128):
	for j in xrange(128):
		c = grid[(i,j)]
		if c == '#':
			if i > 0:
				x = grid[(i-1,j)]
				if x != '.':
					grid[(i,j)] = x
				elif grid[(i,j)] == '#':
					grp = next_grp()
					grid[(i,j)] = grp
					regions.add(grp)
			if j < 127:
				if grid[(i,j)] == '#':
					grp = next_grp()
					grid[(i,j)] = grp
					regions.add(grp)
				if grid[(i,j+1)] == '#':
					if grid[(i,j)] != '.':
						grid[(i,j+1)] = grid[(i,j)]
					else:
						if grid[(i,j+1)] == '#':
							grp = next_grp()
							grid[(i,j+1)] = grp
							regions.add(grp)

print("Group", grp)
for i in xrange(8):
	for j in xrange(8):
		print("(" + str(grid[(i,j)]) + ")", end = '')
	print()
print("Part 2:", len(regions))



