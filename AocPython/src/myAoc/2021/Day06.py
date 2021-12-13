from collections import defaultdict


data = open('2021/data/day06').readlines()[0].split(',')
days = [80, 256]

for part in [0, 1]:
    fish = map(lambda x: int(x), data)

    d = defaultdict(int)
    for f in fish: d[f]+= 1

    for day in range(days[part]):
        zeros = None
        for k, v in sorted(d.items()):
            if k == 0:
                zeros = v
            else:
                d[k-1]+= v
                del d[k]
        if zeros is not None:
            d[6]+= zeros
            d[8]+= zeros
            d[0]-= zeros

    print('Part %d: %d' % (part+1, sum(d.values())))


# Part 1: 359344
# Part 2: 1629570219571
