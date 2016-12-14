'''
Created on Dec 12, 2016

@author: Mark
'''
import re
from itertools import combinations
import copy

def valid(state):
    return True

def done(state):
    for x in xrange(1, 4):
        if len(state[str(x)]["chips"]) != 0 or len(state[str(x)]["gens"]) != 0:
            return False
    return True

def moves(state):
    states = []
    nextFloors = [(state["floor"] % 4) + 1, ((state["floor"]) - 2 % 4) + 1]
    items = []
    if len(state["e"]) > 0:
        items.extend(list(state["e"]))
    if len(state[str(state["floor"])]["chips"]) > 0:
        items.extend(list(state[str(state["floor"])]["chips"]))
    if len(state[str(state["floor"])]["gens"]) > 0:
        items.extend(list(state[str(state["floor"])]["gens"]))
    for floor in nextFloors:
        for item in items:
            possState = copy.deepcopy(state)
            possState["e"] = item
            possState[str(state["floor"])]["chips"] = possState[str(state["floor"])]["chips"] - set(item)
            possState[str(state["floor"])]["gens"] = possState[str(state["floor"])]["gens"] - set(item)
            possState["floor"] = floor
            if valid(possState):
                states.append(possState)
        for item in combinations(items, 2):
            possState = copy.deepcopy(state)
            possState["floor"] = floor
            possState["e"] = item
            if valid(possState):
                states.append(possState)
    return states

def move(state):
    if done(state) :
            print "Moves:", state["count"]
            state["done"] = True
    for st in moves(state):
        st["count"]+= 1
        move(st)

# count = 1
# for x in xrange(10):
#     print "count", (count % 4) + 1
#     count+=1
# print
# 
# count = 1
# for x in xrange(10):
#     print "count", ((count - 2) % 4) + 1
#     count -= 1
# exit()

with open("data/day11") as f:
    origState = {"e":set(), "floor":1, "done": False,
             "1": {"chips": set(), "gens":set()},
             "2": {"chips": set(), "gens":set()},
             "3": {"chips": set(), "gens":set()},
             "4": {"chips": set(), "gens":set()},
             "count": 0}
    
    i = 1
    for line in f:
        gens = re.findall("(\w+ generator)", line)
        chips = re.findall("(\w+-compatible microchip)", line)
        c = origState[str(i)]
        origState[str(i)]["chips"] = set(chips)
        origState[str(i)]["gens"] = set(gens)
        i+= 1
    state = copy.deepcopy(origState)
    
    while True:
        while not state["done"]:
            move(state)
        state = origState
        
        