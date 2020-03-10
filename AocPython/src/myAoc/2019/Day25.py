import re
import heapq
import sys
from itertools import combinations
from collections import defaultdict

combos = []
final_inv = ['monolith', 'food ration', 'planetoid', 'space law space brochure', 'weather machine', 'jam', 'semiconductor', 'antenna']
for r in range(1, len(final_inv)):
    for comb in combinations(final_inv, 2):
        combos.append(comb)

# for comb in combos:
#     print(comb)

# print(len(combos))
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
    def __init__(self, code, pos=0,relb=0,inp=[],out=''):
        self.code = code
        self.pos = pos
        self.relb = relb
        self.inp = inp
        self.out = out

    def copy(self):
        return Proc(self.code.copy(), self.pos, self.relb, self.inp.copy(), self.out)

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
                # if 'Unrecognized command.\n\nCommand?' in self.out:
                #     print(self.out, end='')
                self.out+= chr(output)
                if self.out.endswith('Command?\n'):
                    # print(self.out)
                    break
                if "PASSWORD" in self.out.upper():
                    print(self.out)
                    sys.exit()
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


def mv_next_room(p, door, visited, force=False):
    cmd = makeInstr(door)
    res = p.run(cmd)
    loc, doors, items, inv = extract_info(res)
    p.run(makeInstr(OPP_DOOR[door]))
    if force or not loc in visited or 'Pressure-Sensitive' in loc or loc == 'Corridor' or loc == 'Hull Breach':
        return res
    else:
        print('BLOCKING ENTRY TO %s' % loc)
        return None


def get_items(p, comb):
    inventory = set()
    visited = set()
    path = []
    room_map = defaultdict(list)
    cmd = makeInstr('east')
    while True:
        res = p.run(cmd)
        loc, doors, items, _ = extract_info(res)
        if loc == 'Security Checkpoint':
            print('IN SECURITY CHECKPOINT')
        visited.add(loc)
        for item in items:
            if item in comb:
                p.run(makeInstr('take ' + item))
        res = p.run(makeInstr('inv'))
        _, __, ___, inv = extract_info(res)
        inventory.update(set(inv))
        # print(inventory)
        moved = False
        for door in doors:
            if not door in room_map[loc]:
                room_map[loc].append(door)
                res = mv_next_room(p, door, visited)
                if res:
                    path.append(OPP_DOOR[door])
                    moved = True
                    cmd = makeInstr(door)
                    break
        if not doors and not path:
            break
        while path and not moved:
            cmd = makeInstr(path.pop())
            res = p.run(cmd)
            loc, doors, items, _ = extract_info(res)
            if loc == 'Security Checkpoint':
                print('IN SECURITY CHECKPOINT')
            for door in doors:
                if not door in room_map[loc]:
                    #This check is keeping us fom entering the security checkpoint
                    #But if we force entry, we only get 3 items before exiting
                    #We're blocked from getting into some other room that leads to security checkpoint
                    res = mv_next_room(p, door, visited, False)
                    if res:
                        cmd = makeInstr(door)
                        moved = True
                        break
    return (sorted(visited), sorted(inventory))

def find_items(p, door, visited, inventory):
    cmd = makeInstr(door)
    res = p.run(cmd)
    loc, doors, items, _ = extract_info(res)
    if loc in visited: return
    if loc == 'Security Checkpoint':
        res = p.run(makeInstr('inv'))
        _, __, ___, inv = extract_info(res)
        print('In security checkpoint with %d items' % len(inv))
        p.run(makeInstr(OPP_DOOR[door]))
        visited.add(loc)
        return find_items(p.copy(), door, visited, inventory)
    visited.add(loc)
    for item in items:
        if item != 'infinite loop' and item != 'giant electromagnet' and item != 'escape pod' and item != 'photons':
        # if item in comb:
            p.run(makeInstr('take ' + item))
    res = p.run(makeInstr('inv'))
    _, __, ___, inv = extract_info(res)
    inventory.update(set(inv))
    # print(inventory)
    for _door in doors:
        # if _door != OPP_DOOR[door]:
            find_items(p.copy(), _door, visited, inventory)
                
# for comb in combos:
#     p = Proc(code.copy())
#     inv = get_items(p, comb)

# LOOP
p = Proc(code.copy())
rooms, inv = get_items(p, final_inv)
print(rooms)
print(inv)
print('Found %d items from %d rooms' % (len(inv), len(rooms)))

# RECURSIVE
# p = Proc(code.copy())
# visited = set()
# inventory = set()
# find_items(p, 'east', visited, inventory)
# print(visited)
# print(inventory)

# MANUAL
# p = Proc(code.copy())
# cmd = []
# while True:
#     res = p.run(cmd)
#     print(res)
#     loc, doors, items, inv = extract_info(res)
#     # print('Loc: %s' % loc)
#     # print('Doors: %s' % (doors))
#     # print('Items: %s' % (items))
#     # print('Inventory: %s' % (inv))
#     inp = input(':')
#     cmd = makeInstr(inp)

#Go ino rooms not visited, keeping a breadcrumb trail of reverse moves. If you have nowhere to go, reverse one room and
#try again to go into rooms not visited
