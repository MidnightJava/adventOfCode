'''
Created on Dec 15, 2015

@author: maleone
'''

import re
from _collections import defaultdict
from collections import namedtuple
        
ingredients = defaultdict()
maxVal = 0
Props = namedtuple('Props', 'cap dur flav text cal')
regex = '^(\w+)\:\s\w+\s(\-?\d+)\,\s\w+\s(\-?\d+)\,\s\w+\s(\-?\d+)\,\s\w+\s(\-?\d+)\,\s\w+\s(\-?\d+)$'

def calc(comb, cals):
    results = 1
    cal = 0
    for i in xrange(0, 4):
        res = 0
        for j in xrange(0, len(ingredients.values())):
            res += comb[j] * ingredients.values()[j][i]
        results *= res if res > 0 else 0
    for j in xrange(0, len(ingredients.values())):
            cal += comb[j] * ingredients.values()[j][4]
    return results if cals == None or cal == cals else 0

with open("ingredients.txt") as f:
    for line in f:
        name, cap, dur, flav, text, cal = re.findall(regex, line)[0]
        ingredients[name] = [int(cap), int(dur), int(flav), int(text), int(cal)]
    for i in xrange(0, 101):
        for j in xrange(0, 101- i):
            for k in xrange(0, 101 - j - i):
                val = calc((i, j, k, 100 - i - j - k), 500) # None for part1, 500 for part2
                maxVal = val if val > maxVal else maxVal
    
print "Highest score: ", maxVal      