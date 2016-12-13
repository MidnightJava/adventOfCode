'''
Created on Dec 12, 2016

@author: Mark
'''
import re
from itertools import combinations
import copy

def moves(state):
    states = []
    nextFloors = [(state.floor + 1) % 4, (state.floor - 1) % 4]
    items = []
    items.extend(state.e, *state[str(state.floor)])
    for floor in nextFloors:
        for item in items:
            possState = copy.deepcopy(state)
            possState.floor = floor
            possState.e = item
            if valid(possState):
                states.append(possState)
        for item in combinations(items, 2):
            possState = copy.deepcopy(state)
            possState.floor = floor
            possState.e = item
            if valid(possState):
                states.append(possState)
    return states

def move(state):
    if done(state) :
            print "Moves:", state.count
            exit()
    for st in moves(state):
        st.count+= 1
        move(st)


with open("data/day11") as f:
    state = {"e":{}, "floor":1,
             "1": {"chips": [], "gens":[]},
             "2": {"chips": [], "gens":[]},
             "3": {"chips": [], "gens":[]},
             "4": {"chips": [], "gens":[]},
             "count": 0}
    i = 1
    for line in f:
        gens = re.findall("(\w+) generator", line)
        chips = re.findall("(\w+)-compatible microchip", line)
        state[str(i)].chips = chips
        state[str(i)].gens = gens
        i+= 1
        
    move(state)
        
        