import pprint as _pprint
from math import ceil
from math import floor
from collections import defaultdict
pprint = _pprint.PrettyPrinter().pprint
_map = {}
ore_sources = set()

f = open('2019/data/day14d')
for line in f:
    parts = line.split('=>')
    _prod = parts[1].split()
    prod = _prod[1].strip()
    inpl = parts[0].split(',')
    _inpl = []
    for inp in inpl:
        _inp = inp.split()
        _inpl.append((int(_inp[0].strip()), _inp[1].strip()))
        if _inp[1] == 'ORE': ore_sources.add(prod)
    _map[prod] = [int(_prod[0].strip()), _inpl]

pprint(_map)
print(ore_sources)

ore_needed_dict = defaultdict(int)
extra_ore_dict = defaultdict(int)
def get_ore(ele, needed):
    global ore_needed_dict
    ingredients = _map[ele][1]
    yld = _map[ele][0]
    need = ceil(float(needed) / float(yld))
    for chem in ingredients:
        if chem[1] in ore_sources:
            ore_needed_dict[chem[1]]+=( chem[0] * need)
            extra_ore_dict[chem[1]]+= (_map[chem[1]][0] * need)
        else:
            get_ore(chem[1], chem[0] * need)

get_ore('FUEL', 1)
pprint(ore_needed_dict.items())
pprint(extra_ore_dict.items())
ore = 0
for k,v in ore_needed_dict.items():
    yld = _map[k][0]
    quantum = _map[k][1][0][0]
    
    #Use quantized value of ore in setting values in ore_users_dict
    #And calculate excess over what was actually needed
    #net_ore = actual - excess
    #ore_used = next value up from net_ore that is a mult of _map[k][0]
    #Ex a for item A: ore_used = 40; excess = 12; net_ore = 28
    #so we actually used 30, since it comes in quantities of 10
    #ore_used-= extra_ore
    if v % _map[k][0] != 0:
        for i in range(v, v + _map[k][0]):
            if i % _map[k][0] == 0:
                v = i
                break
    ore_used = ceil(float(v) / float(yld)) * quantum
    ore+= ore_used

print('Part 1: %d' % ore)

# Part 1: 637,682 too low, 10,645,906 too high not 1,693,718

"""
Test Answers:

a: 31 correct
b: 165 correct
c: 13312 correct
d: 180697
e: 2210736

"""