import pprint as _pprint
from math import ceil
from math import floor
from collections import defaultdict
pprint = _pprint.PrettyPrinter().pprint
_map = {}
ore_products = set()

f = open('2019/data/day14')
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

# pprint(_map)
# pprint('ore products: %s' % ore_products)

def next_mod_up(n, mod):
    while n % mod !=0:
        n+= 1
    return n
    
def get_ore(ele, needed):
    ingredients = _map[ele][1]
    yld = _map[ele][0]
    need = ceil(float(needed) / float(yld))
    
    for chem in ingredients:
        need2 = need * chem[0]
        yld2 = _map[chem[1]][0]
        if extra[chem[1]]:
            used = extra[chem[1]]
            need2-= used
            extra[chem[1]]-= used
        if need2 % yld2 != 0:
            orig_need = need2
            need2 = next_mod_up(need2, yld2)
            excess = need2 - orig_need
            extra[chem[1]]+= excess
        if chem[1] in ore_products:
            ore_prod_counts[chem[1]]+= need2
        else:
            get_ore(chem[1], need2)

fuel = 1
lastFuel = None
minFuel = 1.
maxFuel = 1e7
target_ore = 1e12
overshoot = 1e5
while True:
    extra = defaultdict(int)
    ore = 0
    ore_prod_counts = defaultdict(int)
    get_ore('FUEL', fuel)
    for k,v in ore_prod_counts.items():
        v = v - extra[k]
        yld = _map[k][0]
        quant = _map[k][1][0][0]
        ore+= (ceil(float(v) / yld)  * quant)
    if fuel == 1:
        print('Part 1: %d' % ore)
    if ore >= target_ore and ore <= target_ore + overshoot:
        break
    else:
        lastFuel = fuel
        if ore > target_ore:
            maxFuel = fuel
        else:
            minFuel = fuel
        fuel = minFuel + int((maxFuel - minFuel) / 2)
print('Part 2: %d' % lastFuel)

#Part 1: 1582325
#Part 2: 2267486