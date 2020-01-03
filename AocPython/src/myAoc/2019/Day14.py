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
    yld = int(_prod[0].strip())
    name = _prod[1].strip()
    ingredients = parts[0].split(',')
    if len(ingredients)== 1 and ingredients[0].split()[1] == 'ORE':
        ore_products.add(name)
    _ingrl = []
    for ingr in ingredients:
        _ingr = ingr.split()
        _ingrl.append((int(_ingr[0].strip()), _ingr[1].strip()))
    _map[name] = [yld, _ingrl]

# pprint(_map)
# pprint('ore products: %s' % ore_products)
    
def make_comp(comp, needed):
    reactants = _map[comp][1]
    yld = _map[comp][0]
    need = ceil(float(needed) / float(yld))
    
    for reactant in reactants:
        need2 = need * reactant[0]
        yld2 = _map[reactant[1]][0]
        if extra[reactant[1]]:
            used = extra[reactant[1]]
            need2-= used
            extra[reactant[1]]-= used
        if need2 % yld2 != 0:
            orig_need = need2
            need2 = need2 // yld2 * yld2 + yld2
            excess = need2 - orig_need
            extra[reactant[1]]+= excess
        if reactant[1] in ore_products:
            ore_prod_counts[reactant[1]]+= need2
        else:
            make_comp(reactant[1], need2)

fuel = 1
lastFuel = None
minFuel = 1.
maxFuel = 1e7
target_ore = 1e12
tolerance = 1e5
while True:
    extra = defaultdict(int)
    ore = 0
    ore_prod_counts = defaultdict(int)
    make_comp('FUEL', fuel)
    for k,v in ore_prod_counts.items():
        yld = _map[k][0]
        quant = _map[k][1][0][0]
        ore+= (ceil(float(v) / yld)  * quant)
    if fuel == 1:
        print('Part 1: %d' % ore)
    if abs(ore - target_ore) <= tolerance:
        break
    else:
        if ore > target_ore:
            maxFuel = fuel
        else:
            minFuel = fuel
        lastFuel = fuel
        fuel = minFuel + int((maxFuel - minFuel) / 2)
print('Part 2: %d' % lastFuel)

#Part 1: 1582325
#Part 2: 2267486