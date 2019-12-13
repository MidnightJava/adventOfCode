
from collections import defaultdict

count = 0
bcount = 0
seen = set()
loc = []
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

    def run(self):
        global count, bcount, loc
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
                console.log('INPUT')
                self.code[p1] = inp
                self.pos+= 2
            elif op == 4: #OUTP
                output = self.code[p1]
                count+= 1
                loc.append(int(output))
                if count % 3 == 0:
                    if int(output) == 2 and not (loc[0], loc[1], loc[2]) in seen:
                            bcount+= 1
                            seen.add((loc[0], loc[1], loc[2]))
                            loc = []
                # if inp is not None: print(output, end='')
                self.pos+= 2
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
                output = "HALT"
                print('%d blocks' % bcount)
                break
            else:
                print('Bad Instruction: %d' % op)
                break
        return output

for part in [1, 2]:

    f = open('./2019/data/day13')
    code = list(map(int, f.readline().split(',')))
    [code.append(0) for _ in range(10000)]
    p = Proc(code)
    res = p.run()
       

#Part 1: 1967
#Part 2: KBUEGZBK
    