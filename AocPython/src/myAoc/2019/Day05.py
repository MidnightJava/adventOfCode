#Part 1
with open('./2019/data/day05') as f:
    inp = f.readline().split(',')
    input = 1
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
            incr = 4
        elif op == 2:
            p1 = inp[pos+1] if m1 else inp[int(inp[pos+1])]
            p2 = inp[pos+2] if m2 else inp[int(inp[pos+2])]
            inp[int(inp[pos+3])] = str(int(p1) * int(p2))
            incr = 4
        elif op == 3:
            inp[int(inp[pos+1])] = str(input)
            incr = 2
        elif op == 4:
            p1 = inp[pos+1] if m1 else inp[int(inp[pos+1])]
            output = p1
            incr = 2
        elif op == 99:
            print('Part 1: %s' % output)
            break
        else:
            print('Bad Instruction: %d' % op)
            break
        pos+= incr

# Part 2
with open('./2019/data/day05') as f:
    inp = f.readline().split(',')
    input = 5
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
            inp[int(inp[pos+1])] = str(input)
            pos+= 2
        elif op == 4:
            p1 = inp[pos+1] if m1 else inp[int(inp[pos+1])]
            output = p1
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

# Part 1: 10987514
# Part 2: 14195011
