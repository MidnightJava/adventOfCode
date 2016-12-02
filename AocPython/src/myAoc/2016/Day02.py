'''
Created on Dec 2, 2016

@author: maleone
'''
from __future__ import print_function
from functools import reduce

btnMap = {"1":(None,None,3,None),
          "2":(None,3,6,None),
          "3":(1,4,7,2),
          "4":(None,None,8,3),
          "5":(None,6,None,None),
          "6":(2,7,"A",5),
          "7":(3,8,"B",6),
          "8":(4,9,"C",7),
          "9":(None,None,None,8),
          "A":(6,"B",None,None),
          "B":(7,"C","D","A"),
          "C":(8,None,None,"B"),
          "D":("B",None,None,None)
          }
instrMap = {"U":0,"R":1,"D":2,"L":3}
def p2(btn, instr):
    n = btnMap[str(btn)][instrMap[instr]]
    if n == None:
        return btn
    return n

def p(btn, instr):
    if btn == None:
        btn = 5;
    if instr == "L":
        n = btn - 1
        if n <1 or n % 3 == 0:
            n = btn
        return n
    elif instr == "R":
        n = btn + 1
        if n > 9 or btn % 3 == 0:
            n = btn
        return n
    elif instr == "U":
        n = btn - 3
        if n < 2:
            n = btn
        return n
    elif instr == "D":
        n = btn + 3
        if n > 9:
            n = btn
        return n
    else:
        print("BAD", btn, instr)

with open("data/day02") as f:
    b = 5
    #part 1
    for line in f:
        button = reduce(lambda x,y: p(x,y), list(line.strip()), b)
        b = button
        print(button, end="")
#part2
with open("data/day02") as f:
    b = 5
    print("Part 2")
    for line in f:
        button = reduce(lambda x,y: p2(x,y), list(line.strip()), b)
        b = button
        print(button, end="")      
    