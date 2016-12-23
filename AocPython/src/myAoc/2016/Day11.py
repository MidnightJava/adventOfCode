'''
Created on Dec 12, 2016

@author: Mark
'''
import re, uuid, copy, md5
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
#     if len(state["e"]) < 1 or len(state["e"]) > 2:
#         print "ELEVATOR INVALID LENGTH"
#         return False
#     if state["count"] >= 800:
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
    if state["floor"] == 1:
        nextFloors.append(2)
    elif state["floor"] == 2:
        nextFloors.extend([3, 1])
    elif state["floor"] == 3:
        nextFloors.extend([4, 2])
    elif state["floor"] == 4:
        nextFloors.append(3)
        
    for floor in nextFloors:
        possState = copy.deepcopy(state)
        possState["floor"] = floor
        possState["count"]+= 1
        possState["id"] = uuid.uuid4().get_urn()
        if valid(possState):
            states.append(possState)
    
    chips = state[str(state["floor"])]["chips"]
    gens = state[str(state["floor"])]["gens"]
    for floor in nextFloors:
        for chip in chips:
            possState = copy.deepcopy(state)
            possState["e"] = set()
            possState[str(state["floor"])]["chips"].remove(chip)
            possState[str(floor)]["chips"].add(chip)
            possState["e"].add(chip)
            possState["floor"] = floor
            possState["count"]+= 1
            possState["id"] = uuid.uuid4().get_urn()
            if valid(possState):
                states.append(possState)
        for gen in gens:
            possState = copy.deepcopy(state)
            possState["e"] = set()
            possState[str(state["floor"])]["gens"].remove(gen)
            possState[str(floor)]["gens"].add(gen)
            possState["e"].add(gen)
            possState["floor"] = floor
            possState["count"]+= 1
            possState["id"] = uuid.uuid4().get_urn()
            if valid(possState):
                states.append(possState)
                
        for chip in chips:
            for gen in gens:
                possState = copy.deepcopy(state)
                possState["e"] = set()
                possState[str(state["floor"])]["gens"].remove(gen)
                possState[str(state["floor"])]["chips"].remove(chip)
                possState[str(floor)]["gens"].add(gen)
                possState[str(floor)]["chips"].add(chip)
                possState["e"].add(gen)
                possState["e"].add(chip)
                possState["floor"] = floor
                possState["count"]+= 1
                possState["id"] = uuid.uuid4().get_urn()
                if valid(possState):
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
    print "Count:", state["count"]
    for i in xrange(1, 5):
        print "Floor", i
        print "\tChips:", ",".join([x.replace("-compatible microchip", "") for x in state[str(i)]["chips"]])
        print "\tGenerators:", ",".join([x.replace(" generator", "") for x in state[str(i)]["gens"]])

def solve(queue):
    global hwm
    while queue:
        state = queue.pop()
#         print "Solve state"
#         printstate(state)
        if state["count"] > hwm:
            hwm = state["count"]
            print "Highest Count", hwm
        if done(state) :
                print "\t***********Moves*************:", state["count"]
                state["done"] = True
                counts.append(state["count"])
                continue
        states = moves(state)
#         if len(states) > 0:
#             print len(states), "states"
        for st in states:
            if done(st) :
                print "\t***********Moves*************:", st["count"]
                st["done"] = True
                counts.append(st["count"])
                continue
            else:
#                 print "next state"
#                 printstate(st)
    #             if st["count"] <= 500:
                queue.insert(0, st)

with open("data/day11") as f:
    state = {"e": set(), "floor":1, "done": False,
             "1": {"chips": set(), "gens": set()},
             "2": {"chips": set(), "gens": set()},
             "3": {"chips": set(), "gens": set()},
             "4": {"chips": set(), "gens":set()},
             "count": 0,
             "id": uuid.uuid4().get_urn()}
    
    i = 1
    for line in f:
        gens = re.findall("(\w+ generator)", line)
        chips = re.findall("(\w+-compatible microchip)", line)
        state[str(i)]["chips"] = set(chips)
        state[str(i)]["gens"] = set(gens)
        i+= 1
   
    solve([state])
    print "Counts", counts
        