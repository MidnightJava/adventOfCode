'''
Created on Dec 26, 2015

@author: Mark
'''

row = 3010
col = 3019
pos = 1
ans = 20151125
for i in xrange(1, row):
    pos += i
    
incr = row + 1
for i in xrange(1, col):
    pos += incr
    incr += 1
print "pos", pos
for i in xrange(pos -1):
    d, m = divmod(ans * 252533,33554393)
    ans = m
    
print ans