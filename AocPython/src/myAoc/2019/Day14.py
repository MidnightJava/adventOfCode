import pprint as _pprint
from math import ceil
from math import floor
from collections import defaultdict
pprint = _pprint.PrettyPrinter().pprint
_map = {}
extra = defaultdict(int)
ore = 0

f = open('2019/data/day14b')
for line in f:
    parts = line.split('=>')
    _prod = parts[1].split()
    prod = _prod[1].strip()
    inpl = parts[0].split(',')
    _inpl = []
    for inp in inpl:
        _inp = inp.split()
        _inpl.append((int(_inp[0].strip()), _inp[1].strip()))
    _map[prod] = [int(_prod[0].strip()), _inpl]

pprint(_map)

ore_needed_dict = defaultdict(int)
extra_ore_dict = defaultdict(int)
def get_ore(ele, needed):
    global ore
    ingredients = _map[ele][1]
    yld = _map[ele][0]
    need = ceil(float(needed) / float(yld))
    if ele == 'ORE':
        ore+= (need * _map[ele][0])
        return
    for chem in ingredients:
        if chem[1] == 'ORE':
            ore+= (chem[0] * need)
            return
        elif extra[chem[1]] and need > chem[0]:
            used = min(need, extra[chem[1]])
            need-= used
            extra[chem[1]]-= used
        if (chem[0] * need ) <_map[chem[1]][0]:
            excess = _map[chem[1]][0] - (chem[0] * need )
        else:
            excess = (chem[0] * need ) % _map[chem[1]][0]
        extra[chem[1]]+= excess
        get_ore(chem[1], chem[0] * need)

get_ore('FUEL', 1)
for k,v in extra.items():
    if _map[k][1][0][1] == 'ORE':
        excess = v
        while excess >= _map[k][0]:
            ore-= _map[k][1][0][0]
            excess-= _map[k][1][0][0]
print('Part 1: %d' % ore)
pprint(extra)

# Part 1: 637,682 too low, 10,645,906 too high not 1,693,718

"""
Test Answers:

a: 31 correct
b: 165 correct
c: 13312 correct
d: 180697 (NVRD: 551, VJHF: 1989, MNCFX: 4192)
e: 2210736

"""