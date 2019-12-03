for n in range(100):
    for v in range(100):
        f = open('./data/day02')
        inp = list(map(lambda x: int(x), f.readline().split(',')))
        inp[1] = n
        inp[2]= v
        pos = 0
        while inp[pos] != 99:
            op = inp[pos]
            if op == 1:
                inp[inp[pos+3]] = inp[inp[pos+1]] + inp[inp[pos+2]]
            elif op == 2:
                inp[inp[pos+3]] = inp[inp[pos+1]] * inp[inp[pos+2]]
            pos+= 4
        if n == 12 and v == 2:
            print('Part 1: %d' % inp[0])
        elif inp[0] == 19690720:
            print('Part 2: %d' % (n*100+v))

# Part 1: 3790645
# Part 2: 6577