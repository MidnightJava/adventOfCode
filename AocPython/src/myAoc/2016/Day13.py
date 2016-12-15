'''
Created on Dec 14, 2016

@author: maleone
'''

from __future__ import print_function

import copy

counts = []
# matrix = []
    
tx = 7
ty = 4
em = -1

def movex(state, xdel):
    state = copy.deepcopy(state)
    state["x"]+= xdel
    state["cnt"]+= 1
    return None if state["x"] < 0 or isWall(state["x"], state["y"]) else state

def movey(state, ydel):
    state = copy.deepcopy(state)
    state["y"]+= ydel
    state["cnt"]+= 1
    return None if state["y"] < 0 or isWall(state["x"], state["y"]) else state
    
    
def isWall(x, y):
    a = x*x + 3*x + 2*x*y + y + y*y + 10
    b = bin(a)
    numBits = b.count("1")
    return True if numBits % 2 != 0 else False

done = False

for y in xrange(7):
#     row = list()
    print()
    for x in xrange(10):
        print("#" if isWall(x, y) else ".", end="")
print()
#     matrix.append(row)

# def run(state):
#     global counts
#     lc = []
#     for x in [0,1]:
#         for y in [0, 1]:
#             st = move(state, x, y)
#             if st:
#                 if st["x"] == tx and st["y"] == ty:
#                     lc.append(st["cnt"])
#                     print "target reached: ", st["cnt"]
#                 else:
#                     run(st)
#     counts.add(min(lc))
#     print min(counts)

def run(state):
    global counts
    lc = []
    state = copy.deepcopy(state)
    xdiff = abs(tx - state["x"])
    done = blocked = False
    while not done:
        while xdiff >= em and not done and not blocked:
            xdir = 1 if tx - state["x"] > 0 else -1
            st = movex(state, xdir)
            if st:
                if st["x"] == tx and st["y"] == ty:
                    done = True
                    lc.append(st["cnt"])
                    print("Done", st["cnt"])
                else:
                    state = st
                    xdiff = abs(tx - state["x"])
            else:
                blocked = True
                
        if not done:
            ydiff = abs(ty - state["y"])
            blocked = False
            while ydiff >= em and not done and not blocked:
                ydir = 1 if ty - state["y"] > 0 else -1
                st = movey(state, ydir)
                if st:
                    if st["x"] == tx and st["y"] == ty:
                        done = True
                        lc.append(st["cnt"])
                        print("Done", st["cnt"])
                    else:
                        state = st
                        ydiff = abs(ty - state["y"])
                else:
                    blocked = True     
    print("loop")        
    
    print("Total", lc)
    
state = {"x":1, "y":1, "cnt":0}
run(copy.deepcopy(state))
