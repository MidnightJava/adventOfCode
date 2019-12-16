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

ore_users_dict = defaultdict(int)
def get_ore(ele, needed):
    global ore_users_dict
    ingredients = _map[ele][1]
    yld = _map[ele][0]
    need = ceil(float(needed) / float(yld))
    for chem in ingredients:
        if chem[1] in ore_sources:
            ore_users_dict[chem[1]]+=(chem[0] * need)
        else:
            get_ore(chem[1], chem[0] * need)

get_ore('FUEL', 1)
pprint(ore_users_dict.items())
ore = 0
for k,v in ore_users_dict.items():
    yld = _map[k][0]
    quantum = _map[k][1][0][0]
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