'''
Created on Dec 26, 2016

@author: Mark
'''

from collections import deque
from itertools import permutations

nodes = {}
targets = []
width = 181
height = 39
global start

class Node():
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        if val == '#':
            #wall
            self.val = -100
        elif val == '.':
            #space
            self.val = -1
        elif val == '0':
            #start
            self.val = 0
        else:
            #target
            self.val = int(val)
    
    def __repr__(self):
        return "(" + ",".join([str(self.x),str(self.y),str(self.val)]) + ")"
    
    def neighbors(self):
        delt = [(0,1), (0,-1), (1,0), (-1,0)]
        return [nodes[(x[0] + self.x, x[1] + self.y)] for x in delt if x[0] + self.x >= 0 and x[1] + self.y >= 0 and \
                x[0] + self.x < width and x[1] + self.y < height and \
                nodes[(x[0] + self.x, x[1] + self.y)].val >= -1]
    
def BFS(src, dst):
    seen = set([src])
    queue = deque( [(src, 0)]) 
    while len(queue) > 0:
        node = queue.popleft()
        if repr(node[0]) == repr(dst):
            return node[1]
        if node[0].val < -1:
            continue 
        for nb in node[0].neighbors():
            if not nb in seen and nb.val >= -1:
                queue.append((nb,node[1] + 1))
                seen.add(nb)
    return -1
        
def createPathsDict():
    targetsDict = {}
    targetsDict[start] = {}
    for t in targets:
        d = {}
        for t2 in targets:
            if  repr(t) != repr(t2):
                n = BFS(t, t2)
                d[t2] = n
                print "distance from %d to %d is %d" % (t.val, t2.val, n)
        targetsDict[t] = d
        n = BFS(start, t)
        print "distance from %d to %d is %d" % (start.val, t.val, n)
        targetsDict[start][t] = n
    return targetsDict

with open("data/day24") as f:
    rowNum = 0
    for line in f:
        line = line.strip()
        for i in xrange(len(line)):
            node = Node(i, rowNum, line[i])
            nodes[(i, rowNum)] = node
            if node.val == 0:
                start = node
            elif node.val >= 1:
                targets.append(node)
        rowNum+= 1
    print len(nodes), "nodes created"
    print len(targets), "targets found"

paths = []
paths2 = []
targetPaths = createPathsDict()
perms = permutations(targets)
for targs in perms:
    pathLen = targetPaths[start][targs[0]]
    s = start
    for node in targs[1:]:
        pathLen+= targetPaths[s][node]
        s = node
    paths.append(pathLen)
    pathLen+= targetPaths[start][targs[-1]]
    paths2.append(pathLen)
print "Part 1: %d; Part 2: %d" % (min(paths), min(paths2))
