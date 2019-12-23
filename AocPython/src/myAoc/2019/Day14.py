import pprint as _pprint
from math import ceil
from math import floor
from collections import defaultdict
pprint = _pprint.PrettyPrinter().pprint
_map = {}
extra = defaultdict(int)
ore = 0
ore_products = set()
ore_prod_counts = defaultdict(int)

f = open('2019/data/day14d')
for line in f:
    parts = line.split('=>')
    _prod = parts[1].split()
    prod = _prod[1].strip()
    inpl = parts[0].split(',')
    if len(inpl)== 1 and inpl[0].split()[1] == 'ORE':
        ore_products.add(prod)
    _inpl = []
    for inp in inpl:
        _inp = inp.split()
        _inpl.append((int(_inp[0].strip()), _inp[1].strip()))
    _map[prod] = [int(_prod[0].strip()), _inpl]

pprint(_map)
pprint('ore products: %s' % ore_products)

def get_ore(ele, needed):
    global ore
    ingredients = _map[ele][1]
    yld = _map[ele][0]
    need = ceil(float(needed) / float(yld))
    if extra[ele] >= need:
        used = min(need, extra[ele])
        need-= used
        extra[ele]-= used
        if need == 0: return

    elif need % yld != 0:
        excess = ceil(float(need) / float(yld)) * yld
        if excess > 0:
            extra[ele]+= excess
    for chem in ingredients:
        if chem[1] in ore_products:
            ore_prod_counts[chem[1]]+= (need * chem[0])
        else:
            get_ore(chem[1], chem[0] * need)

get_ore('FUEL', 1)
pprint('extra %s ' % extra)
ore_prod_counts2 = dict()
for k,v in ore_prod_counts.items():
    if v % _map[k][0] !=0:
        yld = _map[k][0]
        ore_prod_counts2[k] = ceil(float(v) / yld) * yld
    else:
        ore_prod_counts2[k] =v
pprint('ore prod counts: %s ' % ore_prod_counts2)
for k,v in ore_prod_counts2.items():
    yld = _map[k][0]
    quant = _map[k][1][0][0]
    ore+= (v / yld  * quant)
print('Part 1: %d' % ore)
# pprint(extra)

# Part 1: 637,682 too low, 10,645,906 too high not 1,693,718

"""
Test Answers:

a: 31 correct
b: 165 correct
c: 13312 correct
d: 180697 (NVRD: 551, JNWZP: 78, VJHF: 1989, MNCFX: 4192)
e: 2210736

"""