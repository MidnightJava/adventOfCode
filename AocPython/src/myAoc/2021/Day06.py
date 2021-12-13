from collections import defaultdict, deque
import time


data = open('2021/data/day06').readlines()[0].split(',')
days = [80, 256]

for part in [0, 1]:
    start = time.time()
    fish = map(lambda x: int(x), data)

    d = deque([0]*9)
    for f in fish: d[f]+= 1

    for day in range(days[part]):
        v = d.popleft()
        d.append(v)
        d[6]+= v

    # Slower solution (my original) usig dict keys instead of a circular buffer   
    # d = defaultdict(int)
    # for f in fish: d[f]+= 1

    # for day in range(days[part]):
    #     zeros = None
    #     for k, v in sorted(d.items()):
    #         if k == 0:
    #             zeros = v
    #         else:
    #             d[k-1]+= v
    #             del d[k]
    #     if zeros is not None:
    #         d[6]+= zeros
    #         d[8]+= zeros
    #         d[0]-= zeros

    # print('Part %d: %d Time: %d secs' % (part+1, sum(d.values()), time.time() - start))
    print('Part %d: %d Time: %d secs' % (part+1, sum(d), time.time() - start))


# Part 1: 359344
# Part 2: 1629570219571
