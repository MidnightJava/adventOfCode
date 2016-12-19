'''
Created on Dec 18, 2016

@author: Mark
'''

def parseline(n):
    global data
    row = data[n - 1]
    newRow = []
    for i in xrange(len(row)):
        l,r = (False if i == 0 else row[i-1], False if i == len(row) -1 else row[i+1])
        newRow.append(l ^ r)
    data.append(newRow)
    
inp = ".^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^."
for n in [40, 400000]:
    counts = 0
    data = [[True if c == "^" else False for c in inp]]
    for i in xrange(1, n):
        parseline(i)
    for r in data:
        counts+= r.count(False)
    print counts

