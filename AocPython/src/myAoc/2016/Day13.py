'''
Created on Dec 14, 2016
1,2  2,2 3,2  3,3 3,4  4,4  4,5 5,5  6,5 6,4  7,4
@author: Mark
'''

from collections import deque 

# def fixShortestPath(shortpaths):
#     lastNode = '1,1'
#     index = 0
#     path = []
#     while index < len(shortpaths[0]):
#         node = shortpaths[0][index]
#         skipped = False
#         for y in xrange(index, len(shortpaths[0])):
#             if adj2(lastNode, shortpaths[0][y]):
#                 node = shortpaths[0][y]
#                 index = y + 1
#                 skipped = True
#         
#         path.append(node)
#         lastNode = node
#         if not skipped:
#             index += 1
#     
#     return path
# 
# import networkx as nx
# 
# G = nx.DiGraph()
rows = 50
cols = 50

# count = -1
# scount = 1
# 
# pathCount = 0

grid = []

# path = [(1,1)]

# tx = 7
# ty = 4
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
    
# visited = {}
# v = set()
# # w = set()
# def adj(t1, t2):
#     if t1[0] == t2[0]:
#         return abs(t1[1] - t2[1]) == 1
#     elif t1[1] == t2[1]:
#         return abs(t1[0] - t2[0]) == 1
#     return False
# 
# def adj2(s1, s2):
#     t1 = tuple([int(x) for x in s1.split(",")])
#     t2 = tuple([int(x) for x in s2.split(",")])
#     return adj(t1, t2)
    
grid[tx][ty] = 2

# lastNode = (1,1)
# 
# path2 = set()

def BFS(x, y, seen):
    queue = deque( [(x,y,0)]) #create queue 
    while len(queue)>0: #make sure there are nodes to check left 
        node = queue.popleft() #grab the first node 
        x = node[0] #get x and y 
        y = node[1] 
        if grid[x][y] == 2: #check if it's an exit 
            print 'found at %d,%d' % (x, y)
            return node[2]
        if (grid[x][y] == 1): #if it's not a path, we can't try this spot 
#             print "wall at %d,%d" % (x,y)
            continue 
        grid[x][y]=3 #make this spot explored so we don't try again
        neighbors = [ n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if n[0] >= 0 and n[0] < cols and n[1] >=0 and n[1] < rows ]
        seen[(node[0], node[1])] = node[2]
        for nb in neighbors:
            if not nb in seen or seen[(nb[0], nb[1])] > node[2] :
#                 print "add to queue %d,%d" % (nb[0], nb[1])
                queue.append((nb[0],nb[1],node[2] + 1))
#         for i in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]: #new spots to try 
#             queue.append((i[0],i[1],node))#create the new spot, with node as the parent 
    return -1
            
# def GetPathFromNodes(node): 
#     path = [] 
#     while(node != None): 
#         path.append((node[0],node[1])) 
#         node = node[2] 
#     return path 
#     
# 
# def search(x, y):
#     global path2
#     global scount, pathCount
#     global lastNode, count2
#     global count, visited
#     if grid[x][y] == 2:
#         count+= 1
#         visited[(x, y)] = count
#         pathCount+= 1
#         path2.add((x,y))
#         print 'found at %d,%d' % (x, y), "count", len(v)
#     elif grid[x][y] == 1:
# #         print 'wall at %d,%d' % (x, y)
#         return False
#     elif grid[x][y] == 3:
#         if not (x,y) in visited.keys():
#             path2.add((x,y))
#         count = visited[(x, y)]
#         if not (x,y) in v:
#             scount-=1
#             pathCount+=1
#             v.add((x,y))
#         else:
#             if (x,y) in path2:
#                 path2.remove((x,y))
#             pathCount-= 1
#         return False
#     
#     if not (x,y) in visited.keys():
#         path2.add((x,y))
#     count+= 1
#     pathCount+=1
#     scount+= 1
#     #Don't know why we don't get the right anawer at scount == 50
#     if scount == 48:
#         print "Part 2:", len(visited.keys())
#     
# #     print 'visiting %d,%d, Count: %d' % (x, y, count)
#     visited[(x, y)] = count
#     
#     G.add_edge(",".join((str(lastNode[0]), str(lastNode[1]))), ",".join((str(x),str(y))))
#     lastNode = (x,y)
# 
#     # mark as visited
#     grid[x][y] = 3
#     
#     
#     # explore neighbors clockwise starting by the one on the right
#     if ((x < len(grid)-1 and search(x+1, y))
#         or (y > 0 and search(x, y-1))
#         or (x > 0 and search(x-1, y))
#         or (y < len(grid)-1 and search(x, y+1))):
#         return True
#     return False
# 
# # search(1, 1)
seen = {}
n = BFS(1, 1, seen)
print "BFS shortest path", n
print "Part 2", len([seen[x] for x in seen.keys() if seen[x] <= 50])

# only_containing_nodes = lambda x: True
# all_shortest_paths = nx.all_shortest_paths(G, source=",".join((str(1),str(1))), target=",".join((str(tx),str(ty))))
# # all_simple_paths = nx.all_simple_paths(G, source=",".join((str(1),str(1))), target=",".join((str(tx),str(ty))))
# shortpaths = filter(only_containing_nodes, all_shortest_paths)
# simplepaths = filter(only_containing_nodes, all_simple_paths)
 
# for p in shortpaths:
#     print "Short Path"
#     print p
# for p in simplepaths:
#     print "Simple Path"
#     print p
     
# print "Length:", len(set(*shortpaths))
 
# path = fixShortestPath(shortpaths)
 
# print "dups", len(path) != len(set(path))
# print "Part 1", len(path)
# print path

# def findPaths(G,u,n):
#     allpaths = set()
#     if n==0:
#         return [[u]]
#     paths = [[u]+path for neighbor in G.neighbors(u) for path in findPaths(G,neighbor,n-1) if u not in path]
#     return paths
#     paths = nx.all_pairs_shortest_path(G)
#     for p in paths.values():
#         for v in p.values():
#             allpaths |= set(v)
#     print "Total Length:", len(allpaths)

# allpaths = list()
# for x in xrange(50):
#     paths = findPaths(G, ",".join((str(1),str(1))), x)
#     for p in paths:
#         allpaths.extend(set(p))
# findPaths(G, ",".join((str(1),str(1))), 50)
