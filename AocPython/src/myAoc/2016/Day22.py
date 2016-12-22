'''
Created on Dec 22, 2016

@author: maleone
'''
import re

global nodes, viable

class Node():
    
    def __init__(self, x, y, used, avail):
        self.x = int(x)
        self.y = int(y)
        self.used = int(used)
        self.avail = int(avail)
        
    def id(self):
        return ((self.x, self.y))
        
with open("data/day22") as f:
    nodes = []
    viable = set()
    for line in f:
        res = re.findall("/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T", line)
        if res:
            node = res[0]
            nodes.append(Node(node[0], node[1], node[3], node[4]))

print "total nodes", len(nodes)
for n1 in nodes:
    for n2 in nodes:
        if n1.id() != n2.id() and n1.used != 0 and n1.used <= n2.avail:
            viable.add((n1, n2))

print len(viable), "viable pairs"