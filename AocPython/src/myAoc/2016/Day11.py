'''
Created on Dec 12, 2016

@author: Mark
'''
import re
from itertools import combinations
import copy

def valid(state):
    if len(state["e"]) < 1 or len(state["e"]) > 2:
        return False
    eItems = state["e"]
    gens = state[str(state["floor"])]["gens"]
    chips = state[str(state["floor"])]["chips"]
    for item in eItems:
        if "-compatible microchip" in item:
            chip = item.replace("-compatible microchip", "")
            if not (chip + " generator") in gens and len(gens) > 0:
                return False
        elif " generator" in item:
            gen = item.replace(" generator", "")
            for chip in chips:
                if not chip.startswith(gen) and not chip + " generator" in gens:
                    return False
    return True

def done(state):
    if len(state["4"]["chips"]) + len(state["4"]["gens"]) >= 10:
        return True
    for x in xrange(1, 4):
        if len(state[str(x)]["chips"]) != 0 or len(state[str(x)]["gens"]) != 0:
            return False
    return True

def moves(state):
    states = []
    nextFloors = []
    if state["floor"] == 1:
        nextFloors.append(2)
    elif state["floor"] == 2:
        nextFloors.extend([1, 3])
    elif state["floor"] == 3:
        nextFloors.extend([2, 4])
    elif state["floor"] == 4:
        nextFloors.apped(3)
        
    for floor in nextFloors:
        possState = copy.deepcopy(state)
        possState["floor"] = floor
        if valid(possState):
            states.append(possState)
    
    items = []
    if len(state["e"]) > 0:
        items.extend(state["e"])
    if len(state[str(state["floor"])]["chips"]) > 0:
        items.extend(state[str(state["floor"])]["chips"])
    if len(state[str(state["floor"])]["gens"]) > 0:
        items.extend(state[str(state["floor"])]["gens"])
    for floor in nextFloors:
        for item in items:
            possState = copy.deepcopy(state)
            possState["e"].add(item)
            if item in possState[str(state["floor"])]["chips"]:
                possState[str(state["floor"])]["chips"].remove(item)
            if item in possState[str(state["floor"])]["gens"]:
                possState[str(state["floor"])]["gens"].remove(item)
            possState["floor"] = floor
            if valid(possState):
                states.append(possState)
                
            possState = copy.deepcopy(state)
            possState[str(state["floor"])]["chips"].add(item)
            if item in possState["e"]:
                possState["e"].remove(item)
            if item in possState[str(state["floor"])]["gens"]:
                possState[str(state["floor"])]["gens"].remove(item)
            possState["floor"] = floor
            if valid(possState):
                states.append(possState)
                
            possState = copy.deepcopy(state)
            possState[str(state["floor"])]["gens"].add(item)
            if item in possState["e"]:
                possState["e"].remove(item)
            if item in possState[str(state["floor"])]["chips"]:
                possState[str(state["floor"])]["chips"].remove(item)
            possState["floor"] = floor
            if valid(possState):
                states.append(possState)
        for combo in combinations(items, 2):
            possState = copy.deepcopy(state)
            possState["e"].update(combo)
            for item in combo:
                if item in possState[str(state["floor"])]["chips"]:
                    possState[str(state["floor"])]["chips"].remove(item)
                if item in possState[str(state["floor"])]["gens"]:
                    possState[str(state["floor"])]["gens"].remove(item)
            possState["floor"] = floor
            if valid(possState):
                states.append(possState)
                
            possState = copy.deepcopy(state)
            possState[str(state["floor"])]["chips"].update(set(combo))
            for item in combo:
                if item in possState["e"]:
                    possState["e"].remove(item)
                if item in possState[str(state["floor"])]["gens"]:
                    possState[str(state["floor"])]["gens"].remove(item)
            possState["floor"] = floor
            if valid(possState):
                states.append(possState)
                
            possState = copy.deepcopy(state)
            possState[str(state["floor"])]["gens"].update(set(combo))
            for item in combo:
                if item in possState["e"]:
                    possState["e"].remove(item)
                if item in possState[str(state["floor"])]["chips"]:
                    possState[str(state["floor"])]["chips"].remove(item)
            possState["floor"] = floor
            if valid(possState):
                states.append(possState)
    return states

def move(state):
    print "Count:", state["count"]
    if done(state) :
            print "\t***********Moves*************:", state["count"]
            state["done"] = True
    states = moves(state)
    if len(states) > 0:
        print len(states), "states"
    for st in states:
        if done(st) :
            print "\t***********Moves*************:", st["count"]
            st["done"] = True
        else:
            st["count"]+= 1
            move(st)

with open("data/day11") as f:
    origState = {"e": set(), "floor":1, "done": False,
             "1": {"chips": set(), "gens": set()},
             "2": {"chips": set(), "gens": set()},
             "3": {"chips": set(), "gens": set()},
             "4": {"chips": set(), "gens":set()},
             "count": 0}
    
    i = 1
    for line in f:
        gens = re.findall("(\w+ generator)", line)
        chips = re.findall("(\w+-compatible microchip)", line)
        origState[str(i)]["chips"] = set(chips)
        origState[str(i)]["gens"] = set(gens)
        i+= 1
    state = copy.deepcopy(origState)
    
    while True:
        while not state["done"]:
            move(state)
        state = origState
        
        