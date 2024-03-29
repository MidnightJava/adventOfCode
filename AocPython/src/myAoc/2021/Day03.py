"""
The input consists of a series of string values that represent binary numbers. The
Object is to calulate some binary numbers by manipulating the input numbers. Report
the decimal value of the calculated binary number.

Part 1: Calculate Power Consumptiom, as the product of Gamma and Epsilon. These
quantities are determined one bit at a time, by looking at the corresponding bit
in the entire input stream. For Gamma, assign the most common value at that bit
location among all numbers in the input. For Epsilon, assign the least common value.

Part 2: Calculate Life Support Rating, as the product of Oxygen and CO2. These values
are calcualted by recursively filtering the input values by selecting only the numbers
that satisfy the bit criteria for each bit, considered one a time from left to right,
until only one number remains.

Oxygen bit criteria: Select numbers whose value at the current bit position is the most
common value among all the input numbers.

CO2: Select numbers whose value at the current bit position is the least
common value among all the input numbers.
"""

lines = open('2021/data/day03').readlines()
bits = zip(*lines)

gamma = ''
epsilon = ''

for b in bits:
    ones = b.count('1')
    zeros = b.count('0')
    if ones >= zeros: 
        gamma+= '1'
        epsilon+= '0'
    else:
        gamma+= '0'
        epsilon+= '1'

pc = int(gamma, 2)  * int(epsilon, 2)

print('Part 1: %d' % pc)

for _ in range(len(lines[0])):
    lc = lines[::] # lines copy
    bp = 0 # bit position
    while len(lc) > 1:
        map= list(zip(*lc))
        bs = map[bp] #bit string
        ones = bs.count('1')
        zeros = bs.count('0')
        lc = filter(lambda x: x[bp] == ('1' if ones >= zeros else '0'), lc)
        bp+= 1
    o2 = lc[0]
    break

for _ in range(len(lines[0])):
    lc = lines[::]
    bp = 0
    while len(lc) > 1:
        map= list(zip(*lc))
        bs = map[bp]
        ones = bs.count('1')
        zeros = bs.count('0')
        lc = filter(lambda x: x[bp] == ('0' if ones >= zeros else '1'), lc)
        bp+= 1
    co2 = lc[0]
    break

ls = int(o2, 2) * int(co2, 2)

print('Part 2: %d' % ls)
# Part 1: 2035764
# Part 2: 2817661