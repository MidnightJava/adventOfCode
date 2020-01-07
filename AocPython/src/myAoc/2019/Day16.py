from itertools import cycle

inp = open('2019/data/day16').read()
inp*= 1000
offset = int(inp[:7])
print('Offset', offset)
print('Len input', len(inp))
# inp ="12345678"
# inp ="80871224585914546619083218645595"

for n in range(100):
    outp  = ''
    for j in range(1, len(inp)+1):
        tot = 0
        pattern = cycle([0,1,0,-1])
        p = next(pattern)
        for i in range(1, len(inp)+1):
            if i % j == 0: p = next(pattern)
            v = int(inp[i-1])
            tot+= (v * p)
        outp+= str(tot)[-1]
    inp = outp

# print('Part 1: %s' % outp[:8])
print('Part 2: %s' % outp[offset:])