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
# inp = "03036732577212944063491565474664"
# offset = int(inp[:7])
# print('Offset', offset)
# inp*= 10000
# inp = inp[offset:]
# answ = '84462026'



# for n in range(100):
#     tot = sum(map(int, list(inp)))
#     # print(inp[:8])
#     outp  = ''
#     subtr = 0
#     for j in range(len(inp)):
#         subtr+= int(inp[j])
#         outp+= str(tot - subtr)[-1]
#     inp = outp
#     if answ in outp: print('Found',  n, outp.index(answ))

# print('Part 2: %s' % (inp[:8]))

inps = ["03036732577212944063491565474664", "02935109699940807407585447034323", "03081770884921959731165446850517"]
answs = ['84462026', '78725270', '53553731']
corrections = [7868, 7900, 3932]

for test in range(3):
    inp = inps[test]
    answ = answs[test]
    inp*= 10000
    offset = int(inp[:7])
    print('Offset', offset)
    offset+= + corrections[test]
    print('sum', sum(map(int, list(inp[:7868]))))
    inp = inp[offset:]

    for n in range(100):
        # print('len', len(inp))
        tot = sum(map(int, list(inp)))
        # print(inp[:8])
        outp  = ''
        subtr = 0
        for j in range(len(inp)):
            subtr+= int(inp[j])
            outp+= str(tot - subtr)[-1]
        inp = outp
        if answ in inp: print('Found after %d iterations at offset %d' % (n+1, inp.index(answ)))

    print('Part 2: %s' % inp[:8])

"""
Test Data:
Offset 303673
Len input 320000
"""