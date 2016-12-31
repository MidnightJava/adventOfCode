'''
Created on Dec 14, 2016
1,2  2,2 3,2  3,3 3,4  4,4  4,5 5,5  6,5 6,4  7,4
@author: Mark
'''

from collections import deque 

rows = 50
cols = 50

grid = []

tx = 39
ty = 31

def isWall(x,y):
    a = x*x + 3*x + 2*x*y + y + y*y + 1358
#     a = x*x + 3*x + 2*x*y + y + y*y + 10
    b = bin(a)
    numBits = b.count("1")
    return True if numBits % 2 != 0 else False

for y in xrange(rows):
    row = list()
    for x in xrange(cols):
        row.append(1 if isWall(x, y) else 0)
    grid.append(row)
    
grid[tx][ty] = 2

def BFS(x, y, seen):
    queue = deque( [(x,y,0)]) 
    while len(queue)>0:  
        node = queue.popleft() 
        x = node[0] 
        y = node[1] 
        if grid[x][y] == 2: 
            print 'found at %d,%d' % (x, y)
            return node[2]
        if (grid[x][y] == 1): 
            continue 
        grid[x][y]=3 
        neighbors = [ n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if n[0] >= 0 and n[0] < cols and n[1] >=0 and n[1] < rows ]
        seen[(node[0], node[1])] = node[2]
        for nb in neighbors:
            if not nb in seen or seen[(nb[0], nb[1])] > node[2] :
                queue.append((nb[0],nb[1],node[2] + 1))
    return -1
            

seen = {}
n = BFS(1, 1, seen)
print "BFS shortest path", n
print "Part 2", len([seen[x] for x in seen.keys() if seen[x] <= 50])
