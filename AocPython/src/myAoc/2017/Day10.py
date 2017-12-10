'''
Created on Dec 9, 2017

@author: Mark
'''

size = 256
def getInput(part):
	inp = '189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62'
	if part == 1:
		return map(lambda x: int(x), inp.split(','))
	else:
		suffix = [17, 31, 73, 47, 23]
		lst = []
		for c in inp:
			lst.append(ord(c))
		lst.extend(suffix)
		return lst

def solve(lst, idx, skip, part):
	inp = getInput(part)
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

idx = skip = 0
lst = list(xrange(size))
solve(lst, idx, skip, 1)
print "Part 1:", lst[0] * lst[1]

## Part 2 ##
idx = skip = 0
lst = list(xrange(size))
for i in xrange(64):
	idx, skip = solve(lst, idx, skip, 2)
	
lst2 = []
val = 0
for i in xrange(256):
	val^= lst[i]
	if (i + 1) % 16 == 0:	
		lst2.append(val)
		val = 0

out =''
for v in lst2:
	hval = hex(v)[2:]
	if len(hval) == 1:
		hval = '0' + hval
	out+= hval
print "Part 2:", out


