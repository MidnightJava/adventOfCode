'''
Created on Dec 22, 2015

@author: maleone
'''
from collections import namedtuple

Spell = namedtuple('Spell', 'cost damage heal armor recharge duration ')
spells = []
curent = 0
wins = []
spells.append(Spell(53, 4, 0, 0, 0, 0))
spells.append(Spell(73, 2, 2, 0, 0, 0))
spells.append(Spell(113, 0, 0, 7, 0, 6))
spells.append(Spell(173, 3, 0, 0, 0, 6))
spells.append(Spell(229, 0, 0, 0, 101, 5))

simCount = 0
loseCount = 0
winCount = 0

def validSpells(state):
    _spells = [s for s in spells if s.cost <= state['mana'] and s not in state['effects'].keys()]
    if len(_spells) == 0:
        state['done'] = True
    return _spells

def checkEnd(state):
    global loseCount, winCount
    if state['done']:
        return True
    if state['hit'][1] <= 0:
        wins.append(state['spent'])
        winCount += 1
        state['done'] = True
        return True
    if state['hit'][0] <= 0:
        loseCount += 1
        state['done'] = True
        return True
    return False
    
def sim(state, spell):
    if checkEnd(state): return
    global simCount
    simCount += 1
    for e in state['effects'].keys():
        state['hit'][1] -= e.damage
        state['mana'] += e.recharge
        if e.armor:
            state['armor'] += e.armor if state['effects'][e] == 6 else 0
        if state['effects'][e] == 1:
            state['armor'] -= e.armor
            del state['effects'][e]
        else:
            state['effects'][e] -= 1
    if spell.duration:
        state['effects'][spell] = spell.duration
    else:
        state['hit'][1] -= spell.damage
        state['hit'][0] += spell.heal
    if checkEnd(state): return
    for e in state['effects'].keys():
        state['hit'][1] -= e.damage
        state['mana'] += e.recharge
        if e.armor:
            state['armor'] += e.armor if state['effects'][e] == 6 else 0
        if state['effects'][e] == 1:
            state['armor'] -= e.armor
            del state['effects'][e]
        else:
            state['effects'][e] -= 1
    state['hit'][0] -= max(1, 10 - state['armor'])
    if checkEnd(state): return
    for spell in validSpells(state):
        state['mana'] -= spell.cost
        state['spent'] += spell.cost
        s2 = state.copy()
        sim(s2, spell)
        if s2['done']: return
    

for s in spells:
    state = {'hit':[50,71], 'mana':500, 'armor': 0, 'spent':0, 'effects': {}, 'done': False}
    state['mana'] -= s.cost
    state['spent'] += s.cost
    sim(state, s)
    
print "part 1:", wins, simCount, loseCount, winCount
