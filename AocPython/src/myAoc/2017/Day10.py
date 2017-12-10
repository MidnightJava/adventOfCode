'''
Created on Dec 9, 2017

@author: Mark
'''

inp = [189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62]
text = '189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62'
# text = 'AoC 2017'
suffix = [17, 31, 73, 47, 23]
# inp = [3, 4, 1, 5]

size = 256
# size = 5

lst = list(xrange(size))

skip = 0
idx = 0

inp2 = []
for c in text:
	inp2.append(ord(c))
inp2.extend(suffix)

def solve(byte=False):
	global skip
	global idx
	global lst
	global inp
	if byte:
		inp = inp2
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

solve()
print "Part 1:", lst[0] * lst[1]

lst = list(xrange(size))
idx = 0
skip = 0
for i in xrange(64):
	solve(True)
pos = 0
p2lst = []
# print lst
for i in xrange(16):
	val = 0
	for j in xrange(pos, pos + 16):
		val^= lst[j]
	p2lst.append(val)
	pos+= 16

print p2lst
out =''
for v in p2lst:
	hval = hex(v)[2:]
	if len(hval) == 1:
		hval = '0' + hval
	out+= hval
print "Part 2:", out


