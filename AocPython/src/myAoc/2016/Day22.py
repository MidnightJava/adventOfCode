'''
Created on Dec 22, 2016

@author: maleone
'''
import re
from collections import deque
import copy

global nodes, viable, gr, seen, Infinity

#Over-engineered. Got the shortest path from empty node to goal data, but couldn't
#get a BFS solution for moving the Goal data to the origin. Used the method explained
#here (https://www.reddit.com/r/adventofcode/comments/5jor9q/2016_day_22_solutions/dbhvxkp/)
#to calculate it with a trivial expression.

class Node():
    global emptyNode, goalNode, minSize
    
    def __init__(self, x, y, size, used, avail):
        self.x = int(x)
        self.y = int(y)
        self.size = int(size)
        self.used = int(used)
        self.avail = int(avail)
        self.depth = 0
        
    def id(self):
        return ((self.x, self.y))
    
    def neighbors(self):
        return [n for n in nodes.values() if (((n.x == self.x -1 or n.x == self.x + 1) and n.x >= 0 and n.x < maxX and n.y == self.y) or \
                ((n.y == self.y -1 or n.y == self.y + 1) and n.y >= 0 and n.y < len(nodes) and n.x == self.x)) ]
        
    def __str__(self):
        return str(self.x) + "," + str(self.y)
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
                
def shortestPath(src, dst):
    global p
    seen = set([src])
    queue = deque( [(src, [])]) 
    while queue:
        node = queue.popleft()
        if repr(node[0]) == repr(dst):
            return node[1]
        if node[0].size > 100:
            continue 
        for nb in node[0].neighbors():
            if not nb in seen and not nb in node[1]:
                p = copy.deepcopy(node[1])
                p.append(nb)
                queue.append((nb, p))
                seen.add(nb)
    return -1

maxX = 0
minSize = 1e12
with open("data/day22") as f:
    nodes = {}
    viable = set()
    for line in f:
        res = re.findall("/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T", line)
        if res:
            res = res[0]
            node = Node(res[0], res[1], res[2], res[3], res[4])
            nodes[(node.x, node.y)] = node
            if  node.used == 0:
                emptyNode = node
                print "empty node: %d, %d" % (node.x, node.y)
            maxX = max(maxX, node.x)
            minSize = min(minSize, node.size)
    print  "Max X", maxX
    goalNode = nodes[(maxX, 0)]

for n1 in nodes.values():
    for n2 in nodes.values():
        if n1.id() != n2.id() and n1.used != 0 and n1.used <= n2.avail:
            viable.add((n1, n2))

print len(viable), "viable pairs"

p = []
p = shortestPath(goalNode, emptyNode)
print "Part 2", len(p) + 5 * (maxX -1)

