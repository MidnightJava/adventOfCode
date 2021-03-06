'''
Created on Jan 26, 2019

@author: mal
'''

from __future__ import print_function
import re

imm = {} #immune army
inf = {} #infection army
p_units = '(\d+) units'
p_hitp = '(\d+) hit points'
p_damage = '(\d+) (\w+) damage'
p_init = 'initiative (\d+)'
p_imm = 'immune to ([^\;\)]+)'
p_weak = 'weak to ([^\;\)]+)'

def readData(boost):
    with open('data/Day24')  as f:
        army = imm
        armyname = 'imm'
        _id = 0
        for line in f:
            if line.startswith('Immune System:'): continue
            elif line.startswith('Infection:'):
                army = inf
                armyname = 'inf'
                _id = 0
            else:
                _id+= 1
                g = {}
                g['units'] = int(re.search(p_units, line).group(1))
                g['hitp'] = int(re.search(p_hitp, line).group(1))
                m = re.search(p_damage, line)
                g['dmag'] = int(m.group(1))# damage magnitude
                if army == imm: g['dmag']+= boost
                g['dtype'] = m.group(2) # damage type
                g['init'] = int(re.search(p_init, line).group(1)) #initiative
                m = re.search(p_imm, line)
                if m:
                    g['imm'] = map(lambda x: x.strip(), m.group(1).split(',')) #immune list
                m = re.search(p_weak, line)
                if m:
                    g['weak'] = map(lambda x: x.strip(), m.group(1).split(',')) #weakness list
                g['id'] = armyname + str(_id)
                army[g['id']] = g

def print_armies():
    print('Immune System')       
    for g in imm.values():
        print('%s contains %d units' % (g['id'], g['units']))
     
    print()
    print('Infection')
    for g in inf.values():
        print('%s contains %d units' % (g['id'], g['units']))
    print()

def applyDamage(atckr_id, dfndr_id):
    global inf, imm
    _armies = dict(inf)
    _armies.update(imm)
    if dfndr_id in _armies and atckr_id in _armies:
        dfndr = _armies[dfndr_id]
        atckr = _armies[atckr_id]
        dmg = calc_damage(atckr, dfndr)
        # print('%s attacks %s with damage %d' %(atckr_id,dfndr_id, dmg))
        army = inf if dfndr['id'] in inf else imm
        if dmg > dfndr['units'] * dfndr['hitp']:
            # print('\t%s kills %d units of %s' % (atckr_id, min(dfndr['units'], dmg // dfndr['hitp']), dfndr_id))
            del army[dfndr['id']]
        else:
            # print('\t%s kills %d units of %s' % (atckr_id, dmg // dfndr['hitp'], dfndr_id))
            dfndr['units']-= (dmg // dfndr['hitp'])
            army[dfndr['id']] = dfndr
            
def calc_damage(a, d):
    damage = a['dmag'] * a['units']
    if 'imm' in d and a['dtype'] in d['imm']: damage = 0
    elif 'weak' in d and a['dtype'] in d['weak']: damage*= 2
    return damage
            
# Choose the next target during the targeting phase
def choose_target(g, targets_selected):
    defender = imm if 'inf' in g['id'] else inf
    # candidates:         in the other army       not selected yet                         
    candidates = [c for c in defender.values() if c['id'] not in targets_selected.values()]
    winners = (0, []) # (max_damage, [groups that will inflict the currently max damage]
    for c in candidates:
        damage = calc_damage(g, c)
        if damage == winners[0]:
            winners[1].append(c)
        elif damage > winners[0]:
            winners = (damage, [c])
    # Return damage only for intermediate logging
    damage = winners[0]
    # If more than one group with max damage, choose the one with max effective power and then with max initiative
    winners = sorted(winners[1], key=lambda x: (x['units'] * x['dmag'], x['init']), reverse=True)
    if winners:
        return winners[0], damage
    else:
        return None, damage
            
# Sort groups in the order they will select targets
def target_selection_sort(g):
    # Primary sort key: effective power. Secondary sort key: initiative
    return (g['units'] * g['dmag'], g['init'])
            
# TARGET PHASE
# Sort groups in target selection order, then select a target for each group as applicable
# Return dict: {attacker_id: defender_id}
def target():
    global inf, imm
    armies = inf.values() + imm.values()
    armies = sorted(armies, key=target_selection_sort, reverse=True)
    attacks = {}
    for g in armies:
        # damage returned here only for intermediate logging
        dfndr, dmg = choose_target(g, attacks)
        if dfndr and dmg:
            attacks[g['id']] = dfndr['id']
            # print('%s will attack %s with %d damage' % (g['id'], dfndr['id'], dmg))
    return attacks

# FIGHT PHASE
#
# Do attacks in sorted order
# @param attacks dict: {attacker_id: defender_id}
def fight(attacks):
    _armies = dict(inf, **imm)
    # Attack in decreasing order of initiative
    attk_order = sorted(attacks.keys(), key=lambda x: _armies[x]['init'], reverse=True)
    for attacker in attk_order:
        applyDamage(attacker, attacks[attacker])

def bin_solve(lo, hi):
    mid = lo + (hi - lo) / 2
    readData(mid)
    if hi == lo:
        return solve()[0]
    else:
        iwins = solve()[1]
        return bin_solve(lo, mid) if iwins else bin_solve(mid+1, hi)
    
def total_units(groups):
    return sum([g['units'] for g in groups])

def solve():
    done = False
    while not done:
        units = total_units(inf.values() + imm.values())
        attacks = target()
        fight(attacks)
        if units == total_units(inf.values() + imm.values()):
            return 0, False #fight is a stalemate
        done = not inf or not imm
    
    army = imm or inf
    return total_units(army.values()), army == imm

for part in [1,2]:
    if part == 1:
        readData(0)
        print('Part 1: %s' % solve()[0])
    else:
        print('Part 2: %s' % bin_solve(0, 100))
    
# Part 1 13331
# Part 2: 7476

