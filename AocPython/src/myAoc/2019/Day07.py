from itertools import permutations

#Part 1
outputs = []
input = 0
for phases in permutations([0,1,2,3,4], 5):
    for i in range(5):
        inpCount = 0
        f = open('./2019/data/day07')
        inp = f.readline().split(',')
        pos = 0
        while inp[pos] != 99:
            instr = inp[pos]
            op = int(instr[-2]) * 10 + int(instr[-1]) if len(instr) > 1 else int(instr[0])
            m1 = int(instr[-3]) if len(instr) > 2 else 0
            m2 = int(instr[-4]) if len(instr) > 3 else 0
            if op == 1:
                p1 = inp[pos+1] if m1 else inp[int(inp[pos+1])]
                p2 = inp[pos+2] if m2 else inp[int(inp[pos+2])]
                inp[int(inp[pos+3])] = str(int(p1) + int(p2))
                pos+= 4
            elif op == 2:
                p1 = inp[pos+1] if m1 else inp[int(inp[pos+1])]
                p2 = inp[pos+2] if m2 else inp[int(inp[pos+2])]
                inp[int(inp[pos+3])] = str(int(p1) * int(p2))
                pos+= 4
            elif op == 3:
                if inpCount == 0:
                        inp[int(inp[pos+1])] = str(phases[i])
                        inpCount = 1
                else:
                    if not input is None:
                        inp[int(inp[pos+1])] = str(input)
                        input = None
                pos+= 2
            elif op == 4:
                p1 = inp[pos+1] if m1 else inp[int(inp[pos+1])]
                if i < 4:
                    input = p1
                    break
                else:
                    output = p1
                    if i == 4: outputs.append(int(output))
                    break
                pos+= 2
            elif op == 5:
                p1 = inp[pos+1] if m1 else inp[int(inp[pos+1])]
                p2 = inp[pos+2] if m2 else inp[int(inp[pos+2])]
                pos = int(p2) if int(p1) else pos+3
            elif op == 6:
                p1 = inp[pos+1] if m1 else inp[int(inp[pos+1])]
                p2 = inp[pos+2] if m2 else inp[int(inp[pos+2])]
                pos = int(p2) if not int(p1) else pos+3
            elif op == 7:
                p1 = inp[pos+1] if m1 else inp[int(inp[pos+1])]
                p2 = inp[pos+2] if m2 else inp[int(inp[pos+2])]
                if int(p1) < int(p2):
                    inp[int(inp[pos+3])] = "1"
                else:
                    inp[int(inp[pos+3])] = "0"
                pos+= 4
            elif op == 8:
                p1 = inp[pos+1] if m1 else inp[int(inp[pos+1])]
                p2 = inp[pos+2] if m2 else inp[int(inp[pos+2])]
                inp[int(inp[pos+3])] = "1" if int(p1) == int(p2) else "0"
                pos+= 4
            elif op == 99:
                print('Part 2: %s' % output)
                break
            else:
                print('Bad Instruction: %d' % op)
                break

print('Part 1: %d' % max(outputs))

#Part 2
class Amp:
    def __init__(self, id, code, phase):
        self.id = id
        self.code = code
        self.phase = phase
        self.startup = True
        self.pos = 0
        self.sig = 0

    def set_sig(self, sig):
        self.sig = sig

    def run(self):
        halted = False
        while True:
            instr = self.code[self.pos]
            op = int(instr[-2]) * 10 + int(instr[-1]) if len(instr) > 1 else int(instr[0])
            m1 = int(instr[-3]) if len(instr) > 2 else 0
            m2 = int(instr[-4]) if len(instr) > 3 else 0
            if op == 1: #ADD
                p1 = self.code[self.pos+1] if m1 else self.code[int(self.code[self.pos+1])]
                p2 = self.code[self.pos+2] if m2 else self.code[int(self.code[self.pos+2])]
                self.code[int(self.code[self.pos+3])] = str(int(p1) + int(p2))
                self.pos+= 4
            elif op == 2: #MULT
                p1 = self.code[self.pos+1] if m1 else self.code[int(self.code[self.pos+1])]
                p2 = self.code[self.pos+2] if m2 else self.code[int(self.code[self.pos+2])]
                self.code[int(self.code[self.pos+3])] = str(int(p1) * int(p2))
                self.pos+= 4
            elif op == 3: #INP
                if self.startup:
                    self.code[int(self.code[self.pos+1])] = str(self.phase)
                    self.startup = False
                else:
                    if not self.sig is None:
                        self.code[int(self.code[self.pos+1])] = str(self.sig)
                        self.sig = None
                self.pos+= 2
            elif op == 4: #OUTP
                p1 = self.code[self.pos+1] if m1 else self.code[int(self.code[self.pos+1])]
                self.output = p1
                self.pos+= 2
                break
            elif op == 5: #JMPNZ
                p1 = self.code[self.pos+1] if m1 else self.code[int(self.code[self.pos+1])]
                p2 = self.code[self.pos+2] if m2 else self.code[int(self.code[self.pos+2])]
                self.pos = int(p2) if int(p1) else self.pos+3
            elif op == 6: #JMPZ
                p1 = self.code[self.pos+1] if m1 else self.code[int(self.code[self.pos+1])]
                p2 = self.code[self.pos+2] if m2 else self.code[int(self.code[self.pos+2])]
                self.pos = int(p2) if not int(p1) else self.pos+3
            elif op == 7: #LT
                p1 = self.code[self.pos+1] if m1 else self.code[int(self.code[self.pos+1])]
                p2 = self.code[self.pos+2] if m2 else self.code[int(self.code[self.pos+2])]
                if int(p1) < int(p2):
                    self.code[int(self.code[self.pos+3])] = "1"
                else:
                    self.code[int(self.code[self.pos+3])] = "0"
                self.pos+= 4
            elif op == 8: #EQ
                p1 = self.code[self.pos+1] if m1 else self.code[int(self.code[self.pos+1])]
                p2 = self.code[self.pos+2] if m2 else self.code[int(self.code[self.pos+2])]
                self.code[int(self.code[self.pos+3])] = "1" if int(p1) == int(p2) else "0"
                self.pos+= 4
            elif op == 99: #HALT
                halted = True
                break
            else:
                print('Bad Instruction: %d' % op)
                break
        return (halted, int(self.output))
    

results = []
i = 0
for phases in permutations([5,6,7,8,9], 5):
    amps = []
    for i in range(5):
        f = open('./2019/data/day07')
        code = f.readline().split(',')
        amps.append(Amp(i, code, phases[i]))

    done = False
    i = 0
    output = 0
    while not done:
        amps[i].set_sig(output)
        done, output = amps[i].run()
        if i == 4: results.append(output)
        i = (i+1) % 5

print('Part 2: %d' % max(results))

# Part 1: 440880
# Part 2: 3745599