import re
import heapq

OPP_DOOR = {
    'north' : 'south',
    'south': 'north',
    'east': 'west',
    'west': 'east'
}

def makeInstr(s):
    l = []
    for c in s:
        l.append(ord(c))
        # l.append(ord(','))
    l.append(10)
    return l[::-1]

class Proc:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.relb = 0
        self.inp = []
        self.out = ''

    def get_params(self, modes):
        params = []
        i = 1
        for m in modes:
            params.append(self.code[self.pos+i] if m == 0 else (self.pos+i if m == 1 else self.code[self.pos+i] + self.relb))
            i+= 1
        return params

    def run(self, inp=[]):
        self.inp = inp
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
                if self.inp:
                    self.code[p1] = self.inp.pop()
            elif op == 4: #OUTP
                self.pos+= 2
                output = self.code[p1]
                # print(chr(output), end='')
                self.out+= chr(output)
                if self.out.endswith('Command?\n'):
                    break
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
        res = self.out
        self.out = ''
        return res

def extract_info(s):
    lines = s.split('\n')
    parsing_doors = False
    parsing_items = False
    parsing_inv = False
    items = []
    doors = []
    inv = []
    loc = 'NOT FOUND'
    for line in lines:
        m = re.search('==\s(.*)\s==', line)
        if m:
            loc = m.group(1)
        if line == 'Doors here lead:':
            parsing_items = False
            parsing_doors = True
            parsing_inv = False
            continue
        elif line == 'Items here:':
            parsing_doors = False
            parsing_items = True
            parsing_inv = False
            continue
        elif line == 'Items in your inventory:':
            parsing_doors = False
            parsing_items = False
            parsing_inv = True
            continue
        elif line == '':
            parsing_doors = False
            parsing_items = False
            parsing_inv = False
            continue
        if parsing_items:
            items.append(line.replace('- ', '').strip())
        elif parsing_doors:
            doors.append(line.replace('- ', '').strip())
        elif parsing_inv:
            inv.append(line.replace('- ', '').strip())

    return (loc, doors, items, inv)


f = open('./2019/data/day25')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]

def BFS():
    inventory = set()
    seen = {}
    res = p.run([])
    loc, doors, items, inv = extract_info(res)
    queue = [(0, loc, doors)]
    while queue:
        d, loc, doors = heapq.heappop(queue)
        for door in doors:
            if loc+':'+door not in seen or seen[loc+':'+door] > d:
                seen[loc + ':' + door] = d
                res = p.run(makeInstr(door))
                loc, _doors, items, inv = extract_info(res)
                for item in items:
                    if item != 'infinite loop':
                        p.run(makeInstr('take ' + item))
                res = p.run(makeInstr('inv'))
                _, __, ___, inv = extract_info(res)
                inventory.update(set(inv))
                if 'infinite loop' in items:
                    p.run(makeInstr(OPP_DOOR[door]))
                else:
                    heapq.heappush(queue, (d+1, loc, _doors))
                    break
    return inventory


       

p = Proc(code)
# inv = BFS()
# print(inv)
cmd = []
while True:
    res = p.run(cmd)
    print(res)
    loc, doors, items, inv = extract_info(res)
    # print('Loc: %s' % loc)
    # print('Doors: %s' % (doors))
    # print('Items: %s' % (items))
    # print('Inventory: %s' % (inv))
    inp = input(':')
    cmd = makeInstr(inp)

#Go ino rooms not visited, keeping a breadcrumb trail of reverse moves. If you have nowhere to go, reverse one room and
#try again to go into rooms not visited
