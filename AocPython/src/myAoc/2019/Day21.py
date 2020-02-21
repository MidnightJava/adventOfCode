import re
import sys
import time
from collections import defaultdict
from itertools import permutations
from bitarray import bitarray

intersections = set()
loc = None

output = None
class Proc:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.relb = 0

    def get_params(self, modes):
        params = []
        i = 1
        for m in modes:
            params.append(self.code[self.pos+i] if m == 0 else (self.pos+i if m == 1 else self.code[self.pos+i] + self.relb))
            i+= 1
        return params

    def run(self, inp=[]):
        global output
        while True:
            instr = str(self.code[self.pos])
            op = int(instr[-2]) * 10 + int(instr[-1]) if len(instr) > 1 else int(instr[0])
            modes = [
                int(instr[-3]) if len(instr) > 2 else 0,
                int(instr[-4]) if len(instr) > 3 else 0,
                int(instr[-5]) if len(instr) > 4 else 0
            ]
            p1,p2,p3 = self.get_params(modes) # pylint: disable=unbalanced-tuple-unpacking
            if op == 1: #ADD
                self.code[p3] = self.code[p1] + self.code[p2]
                self.pos+= 4
            elif op == 2: #MULT
                self.code[p3] = self.code[p1] * self.code[p2]
                self.pos+= 4
            elif op == 3: #INP
                self.pos+= 2
                if inp:
                    self.code[p1] = inp.pop()
                else:
                    break
            elif op == 4: #OUTP
                output = self.code[p1]
                self.pos+= 2
                if output <= 127:
                    # print(chr(output), end=' ')
                    pass
                else:
                    return 'DONE'
            elif op == 5:#JMP IF TRUE
                self.pos = self.code[p2] if self.code[p1] else self.pos+3
            elif op == 6:#JMP IF FALSE
                self.pos = self.code[p2] if not self.code[p1] else self.pos+3
            elif op == 7:#LT
                self.code[p3] = 1 if self.code[p1] < self.code[p2] else 0
                self.pos+= 4
            elif op == 8:#EQ
                self.code[p3] = 1 if self.code[p1] == self.code[p2] else 0
                self.pos+= 4
            elif op == 9:#SET RELB
                self.relb+= self.code[p1]
                self.pos+= 2
            elif op == 99:
                # output = 'HALT'
                break
            else:
                print('Bad Instruction: %d' % op)
                break
        return output

def makeInstr(s):
    l = []
    for c in s:
        l.append(ord(c))
        # l.append(ord(','))
    l.append(10)
    return l[::-1]

f = open('./2019/data/day21')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]
proc = Proc(code.copy())
for instr in [ 'NOT A J', 'NOT C T', 'OR T J', 'AND D J']:
    proc.run(makeInstr(instr))
res = proc.run(makeInstr('WALK'))
if res == 'DONE': print('Part 1:', output)

instrs = [
    'NOT C J',
    'AND D J',
    'AND H J',
    'NOT B T',
    'AND D T',
    'OR T J',
    'NOT A T',
    'OR T J'
]

proc = Proc(code.copy())
for instr in instrs:
    proc.run(makeInstr(instr))
res = proc.run(makeInstr('RUN'))
if res == 'DONE': print('Part 2:', output)


"""
Part 1:
    NOT A OR NOT C AND D

Part 2:

@
# # # . # # . # # . # . # # # 

not c and d and h

           @
# # # . # # . # # . # . # # # 

not b and d

(not c and d and h) or (not b and d) or not a

'NOT C J',
'AND D J',
'AND H J',
'NOT B T',
'AND D T',
'OR T J',
'NOT A T',
'OR T J'
"""

# Part 1: 19355364
# Part 2: 1142530574