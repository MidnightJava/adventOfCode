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

# inp = open('2019/data/day16').read()
inp = "03036732577212944063491565474664"
inp*= 10000
answ = '84462026'
offset = int(inp[:7])
print('Offset', offset)


for n in range(100):
    tot = sum(map(int, list(inp[offset:])))
    # print(inp[offset:offset + 8])
    outp  = ''
    subtr = 0
    for j in range(offset+3, len(inp)):
        subtr+= int(inp[j])
        outp+= str(tot - subtr)[-1]
    inp = outp.rjust(len(inp), '0')
    if answ in outp: print('Found',  n, outp.index(answ))

print('Part 2: %s' % (inp[offset:offset+8]))

inp = '02935109699940807407585447034323'
inp*= 10000
answ = '78725270'
offset = int(inp[:7])
print('Offset', offset)


for n in range(100):
    tot = sum(map(int, list(inp[offset:])))
    # print(inp[offset:offset + 8])
    outp  = ''
    subtr = 0
    # print('offset', inp[offset:offset+7])
    for j in range(offset, len(inp)):
        subtr+= int(inp[j])
        outp+= str(tot - subtr)[-1]
    inp = outp.rjust(len(inp), '0')
    if answ in outp: print('Found',  n, outp.index(answ))

# print('Part 2: %s' % res)

"""
Test Data:
Offset 303673
Len input 320000
"""