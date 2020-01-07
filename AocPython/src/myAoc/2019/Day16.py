from itertools import cycle

# inp = open('2019/data/day16').read()
# for n in range(100):
#     outp  = ''
#     for j in range(1, len(inp)+1):
#         tot = 0
#         pattern = cycle([0,1,0,-1])
#         p = next(pattern)
#         for i in range(1, len(inp)+1):
#             if i % j == 0: p = next(pattern)
#             v = int(inp[i-1])
#             tot+= (v * p)
#         outp+= str(tot)[-1]
#     inp = outp

# print('Part 1: %s' % outp[:8])

inp = open('2019/data/day16').read()
inp = "03036732577212944063491565474664"
inp*= 10000
offset = int(inp[:7])
print('Offset', inp[:7], offset)
print('Len input', len(inp))

for n in range(100):
    print("*" + inp[:8] + "*")
    outp  = ''
    tot = sum(map(int, list(inp[offset:])))
    for j in range(offset, len(inp)):
        # pattern = cycle([0,1,0,-1])
        # p = next(pattern)
        for i in range(j, len(inp)):
            # if i % j == 0: p = next(pattern)
            tot-= int(inp[i])
        outp+= str(tot)[-1]
    inp = outp

print('Part 2: %s' % outp)

"""
Test Data:
Offset 303673
Len input 320000
"""