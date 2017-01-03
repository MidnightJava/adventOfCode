'''
Created on Dec 12, 2016

@author: Mark
'''
# Doesn't work
import re, copy, md5
from itertools import combinations
seen = list()
counts = []
hwm = 0

def hashState(state):
    md = md5.new()
    md.update(str(state["floor"]))
    for i in range(1, 5):   
        md.update("".join(sorted(state[str(i)]["chips"])))
        md.update("".join(sorted(state[str(i)]["gens"])))
    return md.hexdigest()

def valid(state):
    if hashState(state) in seen:
        return False
    if len(state["e"]) == 2 and state["e"][0][2] != state["e"][1][2]: #chip and generator
        if state["e"][0][:2] != state["e"][1][:2]:
            return False
#     if len(state["e"]) < 1 or len(state["e"]) > 2:
#         print "ELEVATOR INVALID LENGTH"
#         return False
    eItems = state["e"]
    gens = state[str(state["floor"])]["gens"]
    chips = state[str(state["floor"])]["chips"]
    for chip in chips:
        if (len(gens) > 0 and not chip.replace("-compatible microchip", " generator") in gens):
            return False
    for item in eItems:
        if "-compatible microchip" in item:
            chip = item.replace("-compatible microchip", "")
            if not (chip + " generator") in gens and len(gens) > 0 and not (chip + " generator") in eItems:
                return False
#         elif " generator" in item:
#             gen = item.replace(" generator", "")
#             for chip in chips:
#                 if not chip.startswith(gen) and not (chip.replace("-compatible microchip", " generator") in gens or chip.replace("-compatible microchip", " generator") in eItems):
#                     return False
    seen.append(hashState(state))
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
    
    for i in xrange(1, 5):
        if len(state[str(i)]["chips"]) != 0 or len(state[str(i)]["gens"]) != 0:
            minFloor = i
            break;
    
    if state["floor"] == 1:
        nextFloors.append(2)
    elif state["floor"] == 2:
        nextFloors.extend([3, 1])
    elif state["floor"] == 3:
        nextFloors.extend([4, 2])
    elif state["floor"] == 4:
        nextFloors.append(3)
        
    for floor in nextFloors:
        if floor >= minFloor and floor < state["floor"]:
            possState = copy.deepcopy(state)
            possState["floor"] = floor
            if valid(possState):
                states.append(possState)
    
    chips = state[str(state["floor"])]["chips"]
    gens = state[str(state["floor"])]["gens"]
    noneValid = True
    for floor in nextFloors:
        if floor < minFloor or not noneValid:
            continue
        goingUp = floor > state["floor"]
        for coll, typeName in [(gens, "gens"), (chips, "chips")]:
            if goingUp:
                if len(coll) >= 2:
                    combos = combinations(coll, 2)
                    for combo in combos:
                        possState = copy.deepcopy(state)
                        possState["e"] = list()
                        possState[str(state["floor"])][typeName].remove(combo[0])
                        possState[str(state["floor"])][typeName].remove(combo[1])
                        possState[str(floor)][typeName].add(combo[0])
                        possState[str(floor)][typeName].add(combo[1])
                        possState["e"].append(combo[0])
                        possState["e"].append(combo[1])
                        possState["floor"] = floor
                        if valid(possState):
                            noneValid = False
                            states.append(possState)
                for gen in gens:
                    possState = copy.deepcopy(state)
                    possState["e"] = list()
                    possState[str(state["floor"])]["gens"].remove(gen)
                    possState[str(floor)]["gens"].add(gen)
                    possState["e"].append(gen)
                    if valid(possState):
                        noneValid = False
                        states.append(possState)
                    for chip in chips:
                        possState[str(state["floor"])]["chips"].remove(chip)
                        possState[str(floor)]["chips"].add(chip)
                        possState["e"].append(chip)
                        if valid(possState):
                            noneValid = False
                            states.append(possState)
            else:
                for gen in gens:
                    possState = copy.deepcopy(state)
                    possState["e"] = list()
                    possState[str(state["floor"])]["gens"].remove(gen)
                    possState[str(floor)]["gens"].add(gen)
                    possState["e"].append(gen)
                    possState["floor"] = floor
                    if valid(possState):
                        noneValid = False
                        states.append(possState)
                    for chip in chips:
                        possState[str(state["floor"])]["chips"].remove(chip)
                        possState[str(floor)]["chips"].add(chip)
                        possState["e"].append(chip)
                        if valid(possState):
                            noneValid = False
                            states.append(possState)
                if len(coll) >= 2:
                    combos = combinations(coll, 2)
                    for combo in combos:
                        possState = copy.deepcopy(state)
                        possState["e"] = list()
                        possState[str(state["floor"])][typeName].remove(combo[0])
                        possState[str(state["floor"])][typeName].remove(combo[1])
                        possState[str(floor)][typeName].add(combo[0])
                        possState[str(floor)][typeName].add(combo[1])
                        possState["e"].append(combo[0])
                        possState["e"].append(combo[1])
                        possState["floor"] = floor
                        if valid(possState):
                            noneValid = False
                            states.append(possState)
           
#         for combo in combinations(chips, 2):
#             possState = copy.deepcopy(state)
#             possState["e"] = set()
#             for item in combo:
#                 possState[str(state["floor"])]["chips"].remove(item)
#                 possState[str(floor)]["chips"].add(item)
#                 possState["e"].add(item)
#             possState["floor"] = floor
#             possState["count"]+= 1
#             possState["id"] = uuid.uuid4().get_urn()
#             if valid(possState):
#                 states.append(possState)
#         for combo in combinations(gens, 2):
#             possState = copy.deepcopy(state)
#             possState["e"] = set()
#             for item in combo:
#                 possState[str(state["floor"])]["gens"].remove(item)
#                 possState[str(floor)]["gens"].add(item)
#                 possState["e"].add(item)
#             possState["floor"] = floor
#             possState["count"]+= 1
#             possState["id"] = uuid.uuid4().get_urn()
#             if valid(possState):
#                 states.append(possState)        
            
    return states

def printstate(state):
    print "Floor:", state["floor"]
    for i in xrange(1, 5):
        print "Floor", i
        print "\tChips:", ",".join([x.replace("-compatible microchip", "") for x in state[str(i)]["chips"]])
        print "\tGenerators:", ",".join([x.replace(" generator", "") for x in state[str(i)]["gens"]])

def solve(state, steps, maxSteps ):
    for i in xrange(1, 5):
        if len(state[str(i)]["chips"]) != 0 or len(state[str(i)]["gens"]) != 0:
            minFloor = i
            break;
    print "Trying max steps =", maxSteps, "min non-empty floor", minFloor
    while steps <= maxSteps:
        if done(state) :
            print "\t***********Done*************:", steps
            return steps
        steps+= 1
        states = moves(state)
        for st in states:
            n = solve(copy.deepcopy(st), steps, maxSteps)
            if n:
                return n
    return None

with open("data/day11") as f:
    state = {"e": list(), "floor":1, "done": False,
             "1": {"chips": set(), "gens": set()},
             "2": {"chips": set(), "gens": set()},
             "3": {"chips": set(), "gens": set()},
             "4": {"chips": set(), "gens":set()}}
    
    i = 1
    for line in f:
        gens = map(lambda s: s.replace(" generator", "")[:2] + "G", re.findall("(\w+ generator)", line))
        chips = map(lambda s: s.replace("-compatible microchip", "")[:2] + "M", re.findall("(\w+-compatible microchip)", line))
        state[str(i)]["chips"] = set(chips)
        state[str(i)]["gens"] = set(gens)
        i+= 1
    
    maxSteps = 100
    sol = solve(state, 100, maxSteps)
    while not sol:
        maxSteps+= 1
        sol = solve(copy.deepcopy(state), 100, maxSteps)
    print "Part1", sol
        