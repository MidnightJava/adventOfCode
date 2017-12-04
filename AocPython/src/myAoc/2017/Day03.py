'''
Created on Dec 2, 2017

@author: Mark
'''

### PART 1 ###

val = 0
direction = 0
x = 0
y = 0
incr = 0
target = 361527
while True:
    if val + incr > target:
        incr = target - val
    else:
        incr = (incr + 1) if (direction == 0 or direction == 2) else incr
    val+= incr
    if direction == 0:
        x+= incr
    elif direction == 1:
        y+= incr
    elif direction == 2:
        x-= incr
    elif direction == 3:
        y-= incr
        
    direction = (direction + 1) % 4
        
    if val == target:
        break
    
print "Part 1:", (x if x >= 0 else -x ) + (y if y >= 0 else -y) - 1

### PART 2 ###

class Cell(object):
    def __init__(self, x, y, val=0):
        self.x = x
        self.y = y
        self.val = val
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def nextDir(direc):
    return (direc+1) % 4

def nextCell(cell, direc):
    if direc == 0:
        cell = Cell(cell.x + 1, cell.y)
    elif direc == 1:
        cell = Cell(cell.x, cell.y+1)
    elif direc == 2:
        cell = Cell(cell.x-1, cell.y)
    elif direc == 3:
        cell = Cell(cell.x, cell.y-1)
    return cell

def getVal(cell, visited):
    if cell.x == 0 and cell.y == 0:
        return 1
    val = cell.val
    nbr = Cell(cell.x+1, cell.y)
    if (nbr.x, nbr.y) in visited:
        val+= visited[(nbr.x, nbr.y)]
    nbr = Cell(cell.x, cell.y+1)
    if (nbr.x, nbr.y) in visited:
        val+= visited[(nbr.x, nbr.y)]
    nbr = Cell(cell.x-1, cell.y)
    if (nbr.x, nbr.y) in visited:
        val+= visited[(nbr.x, nbr.y)]
    nbr = Cell(cell.x, cell.y-1)
    if (nbr.x, nbr.y) in visited:
        val+= visited[(nbr.x, nbr.y)]
    nbr = Cell(cell.x+1, cell.y+1)
    if (nbr.x, nbr.y) in visited:
        val+= visited[(nbr.x, nbr.y)]
    nbr = Cell(cell.x-1, cell.y+1)
    if (nbr.x, nbr.y) in visited:
        val+= visited[(nbr.x, nbr.y)]
    nbr = Cell(cell.x-1, cell.y-1)
    if (nbr.x, nbr.y) in visited:
        val+= visited[(nbr.x, nbr.y)]
    nbr = Cell(cell.x+1, cell.y-1)
    if (nbr.x, nbr.y) in visited:
        val+= visited[(nbr.x, nbr.y)]
        
    return val
        

direc = 0
val = 0
cell = Cell(0, 0, 1)
visited = {}
visited[(cell.x, cell.y)] = 1
target = 361527
while True:
    cell = nextCell(cell,direc)
    val = getVal(cell, visited)
    visited[(cell.x, cell.y)] = val
    nxtCell = nextCell(cell, nextDir(direc))
    if (nxtCell.x, nxtCell.y) not in visited:
        direc = nextDir(direc)
    
    if val > target:
        print "Part 2:", val
        break
    
    