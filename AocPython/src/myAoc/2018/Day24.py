'''
Created on Jan 24, 2019

@author: mal
'''

from __future__ import print_function
import re

imm = []
inf = []
p_units = '(\d+) units'
p_hitp = '(\d+) hit points'
p_damage = '(\d+) (\w+) damage'
p_init = 'initiative (\d+)'
p_imm = 'immune to ([^\;\)]+)'
p_weak = 'weak to ([^\;\)]+)'

with open('data/Day24')  as f:
    army = imm
    for line in f:
        if line.startswith('Immune System:'): continue
        elif line.startswith('Infection:'): army = inf
        else:
            g = {}
            g['units'] = int(re.search(p_units, line).group(1))
            g['hitp'] = int(re.search(p_hitp, line).group(1))
            m = re.search(p_damage, line)
            g['dmag'] = int(m.group(1))
            g['dtype'] = m.group(2)
            g['init'] = int(re.search(p_init, line).group(1))
            m = re.search(p_imm, line)
            if m:
                g['imm'] = m.group(1).split(',')
            m = re.search(p_weak, line)
            if m:
                g['weak'] = m.group(1).split(',')
            army.append(g)
            
for g in imm:
    print(g)

print()
 
for g in inf:
    print(g)