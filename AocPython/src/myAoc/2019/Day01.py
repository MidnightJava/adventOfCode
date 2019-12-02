with open('./data/day01') as f:
    fuel_1 = fuel_2 = 0
    for mass in f:
        fuel = int(int(mass) / 3) -2
        fuel_1+= fuel
        fuel_2+= fuel
        while fuel > 0:
            fuel = int(fuel / 3) -2
            if fuel > 0: fuel_2+= fuel

print('Part 1: %d' % fuel_1)
print('Part 2: %d' % fuel_2)

# Part 1: 3560353
# Part 2: 5337642