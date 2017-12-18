'''
Created on Dec 17, 2017

@author: Mark
'''


step = 386
# step = 3


idx = 0

l = 0
while l <= 50000000:
	ol = l
	if l != 0:
		idx = (step + 1) % l
	count = 0
	while idx != 0:
		l+= 1
		idx = (idx + step + 1) % l
		count +=1
	if l == 0:
		l =  1
	else:
		l = (count % l) + 1 + ol
	
print ol -1

#NOT 182353069 NOT 182353070 NOT 46038989





# l = 1227
# ol = l
# idx = (step + 1) % l
# count = 0
# while idx != 0:
# 	l+= 1
# 	idx = (idx + step + 1) % l
# 	count +=1
# print(count % l) + 1 + ol -1

# for i in xrange(10000):
# 	if i != 0:
# 		idx = (idx + step + 1) % len(l)
# 	l.insert(idx, i)
# 	d[l[(l.index(0) + 1) % len(l)]]+= 1
# 	if d[l[(l.index(0) + 1) % len(l)]] == 1:
# 		d2[l[(l.index(0) + 1) % len(l)]] = len(l)
# 
# for key in sorted(d.iterkeys()):
# 	print "%s: %s" % (key, d[key]),"%s" % d2[key]
# # print d2
	
# 	print abs(len(l) - idx)
# 	print l[(l.index(0) + 1) % len(l)]
# 	print i, l[0]

# 	if i == 2017:
# 		print "Part 1:", l[(idx + 1) % len(l)]

# 	if i % 100000 == 0:
# 		print i

# print "Part 2:", l[(l.index(0) + 1) % len(l)]


