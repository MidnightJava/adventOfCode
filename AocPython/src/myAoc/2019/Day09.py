def get_params(modes):
    params = []
    i = 1
    for m in modes:
        params.append(inp[pos+i] if m == 0 else (pos+i if m == 1 else inp[pos+i] + relb))
        i+= 1
    return params

for part in [1, 2]:
    f =  open('./2019/data/day09')
    inp = list(map(int, f.readline().split(',')))
    [inp.append(0) for _ in range(10000)]
    inputs = [1, 2]
    pos = 0
    relb = 0

    while inp[pos] != 99:
        instr = str(inp[pos])
        op = int(instr[-2]) * 10 + int(instr[-1]) if len(instr) > 1 else int(instr[0])
        modes = [
            int(instr[-3]) if len(instr) > 2 else 0,
            int(instr[-4]) if len(instr) > 3 else 0,
            int(instr[-5]) if len(instr) > 4 else 0
        ]
        p1,p2,p3 = get_params(modes) # pylint: disable=unbalanced-tuple-unpacking
        if op == 1: #ADD
            inp[p3] = inp[p1] + inp[p2]
            pos+= 4
        elif op == 2: #MULT
            inp[p3] = inp[p1] * inp[p2]
            pos+= 4
        elif op == 3: #INP
            inp[p1] = inputs[part - 1]
            pos+= 2
        elif op == 4: #OUTP
            output = inp[p1]
            print('Part %d: %d' % (part, output))
            pos+= 2
            break
        elif op == 5:#JMP IF TRUE
            pos = inp[p2] if inp[p1] else pos+3
        elif op == 6:#JMP IF FALSE
            pos = inp[p2] if not inp[p1] else pos+3
        elif op == 7:#LT
            inp[p3] = 1 if inp[p1] < inp[p2] else 0
            pos+= 4
        elif op == 8:#EQ
            inp[p3] = 1 if inp[p1] == inp[p2] else 0
            pos+= 4
        elif op == 9:#SET RELB
            relb+= inp[p1]
            pos+= 2
        elif op == 99:
            print('Halt')
            break
        else:
            print('Bad Instruction: %d' % op)
            break

#Part 1: 2436480432
#Part 2: 45710