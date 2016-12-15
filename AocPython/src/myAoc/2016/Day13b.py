'''
Created on Dec 14, 2016
1,2  2,2 3,2  3,3 3,4  4,4  4,5 5,5  6,5 6,4  7,4
@author: Mark
'''
import copy


rows = 50
cols = 50

count = -1

grid = []

def isWall(y, x):
#     a = x*x + 3*x + 2*x*y + y + y*y + 1358
    a = x*x + 3*x + 2*x*y + y + y*y + 10
    b = bin(a)
    numBits = b.count("1")
    return True if numBits % 2 != 0 else False

for y in xrange(rows):
    row = list()
    for x in xrange(cols):
        row.append(1 if isWall(x, y) else 0)
    grid.append(row)
    
visited = {}
v = set()
w = set()
def adj(t1, t2):
    if t1[0] == t2[0]:
        return abs(t1[1] - t2[1]) == 1
    elif t1[1] == t2[1]:
        return abs(t1[0] - t2[0]) == 1
    return False

def findPath(tup, path):
    path = copy.deepcopy(path)
    global v
    if tup[0] == 7 and tup[1] == 4:
        path.add(tup)
        return path
    found = False
    for t in v:
        if not t in path and adj(t, tup):
            found = True
            path.add(t)
            p = findPath(t, path)
            if p:
                path |= p
    return None if not found else path
    
grid[7][4] = 2
# grid[31][39] = 2

def search(x, y):
    global count, visited
    if grid[x][y] == 2:
        print 'found at %d,%d' % (x, y)
        count+= 1
        print count
        return True
    elif grid[x][y] == 1:
#         print 'wall at %d,%d' % (x, y)
        return False
    elif grid[x][y] == 3:
#         print 'visited at %d,%d' % (x, y)
#         if not (x, y) in visited:
#             count-= 1
#         else:
#             count+= 1
        count = visited[(x, y)]
        v.add((x,y))
        return False
    
    count+= 1
    print 'visiting %d,%d, Count: %d' % (x, y, count)
    visited[(x, y)] = count

    # mark as visited
    grid[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True

    return False

search(1, 1)

print "Answer", findPath((1,1), set())