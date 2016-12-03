'''
Created on Dec 22, 2015

@author: maleone
'''
from collections import namedtuple
import random
from _collections import defaultdict
import collections
import copy

Spell = namedtuple('Spell', 'cost damage heal armor recharge duration ')
spells = []
wins = []
winh = defaultdict(int)
spells.append(Spell(53, 4, 0, 0, 0, 0))
spells.append(Spell(73, 2, 2, 0, 0, 0))
spells.append(Spell(113, 0, 0, 7, 0, 6))
spells.append(Spell(173, 3, 0, 0, 0, 6))
spells.append(Spell(229, 0, 0, 0, 101, 5))

simCount = 0
loseCount = 0
winCount = 0

def validSpells(state):
    _spells = [s for s in spells if s.cost <= state['mana'] and (s not in state['effects'].keys() or state['effects'][s] == 1)]
    return _spells

def checkEnd(state):
    global loseCount, winCount
    if state['part2Done']:
        return True
    if state['hit'][0] <= 0 or state['mana'] <= 0:
        loseCount += 1
        state['part2Done'] = True
        return True
    if state['hit'][1] <= 0:
        wins.append(state['spent'])
        winCount += 1
        state['part2Done'] = True
        return True
    return False

def checkEnd2(state):
    global loseCount, winCount
    if state['part2Done']:
        return True
    if state['hit'][0] <= 0 or state['mana'] <= 0:
        loseCount += 1
        state['part2Done'] = True
        return True, False
    if state['hit'][1] <= 0:
        wins.append(state['spent'])
        winCount += 1
        state['part2Done'] = True
        return True, True
    return False, False
    
def sim(state, spell):
    print min(wins) if wins else None
    global simCount
    simCount += 1
#     state['hit'][0] -= 1 # part 2
    if checkEnd(state):
        return
    delList = []
    for e in state['effects'].keys():
        state['hit'][1] -= e.damage
        state['mana'] += e.recharge
        if state['effects'][e] == 6:
            state['armor'] += e.armor
        if state['effects'][e] == 1:
            state['armor'] -= e.armor
            delList.append(e)
        else:
            state['effects'][e] -= 1
    for x in delList:
        del state['effects'][x]
    delList = []
    if checkEnd(state):
        return
    if spell.duration:
        state['effects'][spell] = spell.duration
    else:
        state['hit'][1] -= spell.damage
        state['hit'][0] += spell.heal
    if checkEnd(state):
        return
    for e in state['effects']:
        state['hit'][1] -= e.damage
        state['mana'] += e.recharge
        if state['effects'][e] == 6:
            state['armor'] += e.armor
        if state['effects'][e] == 1:
            state['armor'] -= e.armor
            delList.append(e)
        else:
            state['effects'][e] -= 1
    for x in delList:
        del state['effects'][x]
    delList = []
    if checkEnd(state):
        return
#     print "armor", state['armor']
    state['hit'][0] -= max(1, 10 - state['armor'])
    if checkEnd(state):
        return
    for spell in validSpells(state):
        s2 = copy.deepcopy(state)
        s2['mana'] -= spell.cost
        s2['spent'] += spell.cost
        sim(s2, spell)    

#Tried this when there was a bug in sim(). Eventually gets the right answer, but takes several minutes
def sim2():
    for i in xrange(1000000):
        state = {'hit':[50,71], 'mana':500, 'armor': 0, 'spent':0, 'effects': {}, 'part2Done': False}
        part2Done = False
        while not part2Done:
            global simCount
            simCount += 1
            state['hit'][0] -= 1 # part 2
            res = checkEnd(state)
            if res[0]:
                if res[1]:
                    wins.append(state['spent'])
                    winh[state['spent']] += 1
                part2Done = True
            for e in state['effects'].keys():
                state['hit'][1] -= e.damage
                state['mana'] += e.recharge
                if state['effects'][e] == 6:
                    state['armor'] += e.armor
                if state['effects'][e] == 1:
                    state['armor'] -= e.armor
                    del state['effects'][e]
                else:
                    state['effects'][e] -= 1
            res = checkEnd(state)
            if res[0]:
                if res[1]:
                    wins.append(state['spent'])
                    winh[state['spent']] += 1
                part2Done = True
            spell = spells[random.randint(0,4)]
            if spell.cost > state['mana'] or (spell in state['effects'].keys() and state['effects'][spell] != 1):
                if len(validSpells(state)) == 0:
                    part2Done = True
                continue
            state['mana'] -= spell.cost
            state['spent'] += spell.cost
            if spell.duration:
                state['effects'][spell] = spell.duration
            else:
                state['hit'][1] -= spell.damage
                state['hit'][0] += spell.heal
            res = checkEnd(state)
            if res[0]:
                if res[1]:
                    wins.append(state['spent'])
                    winh[state['spent']] += 1
                part2Done = True
            for e in state['effects'].keys():
                state['hit'][1] -= e.damage
                state['mana'] += e.recharge
                state['armor'] += e.armor if state['effects'][e] == 6 else 0
                if state['effects'][e] == 1:
                    state['armor'] -= e.armor
                    del state['effects'][e]
                else:
                    state['effects'][e] -= 1
            state['hit'][0] -= max(1, 10 - state['armor'])
            res = checkEnd(state)
            if res[0]:
                if res[1]:
                    wins.append(state['spent'])
                    winh[state['spent']] += 1
                part2Done = True
        if i % 10000 == 0:
            print i, min(wins) if len(wins) > 0 else None

for s in spells:
    state = {'hit':[50,71], 'mana':500, 'armor': 0, 'spent':0, 'effects': {}, 'part2Done': False}
    state['mana'] -= s.cost
    state['spent'] += s.cost
    sim(state, s)

# sim2()
print "Lowest cost to win:", min(wins), simCount, loseCount, winCount
# od = collections.OrderedDict(sorted(winh.items()))
# print od
