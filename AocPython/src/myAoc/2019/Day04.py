count = 0

for x in range(134564, 585159+1):
    match = 0
    xx = str(x)
    # valid = False
    # for i in range(len(xx)):
    #     if i < len(xx)-1 and xx[i] == xx[i+1]:
    #       valid = True
    # if valid:
    mc = 0
    fail = False
    found = False
    for i in range(len(xx)):
        if i < len(xx)-1:
            if xx[i] == xx[i+1]:
                mc+= 1
                if mc >2: fail = True
                elif mc == 2: found = True
            else:
                mc = 0
    if (found or xx[-1] == xx[-2]): match+=1

    valid = True
    for i in range(len(xx)):
        if i < len(xx)-1:
            if int(xx[i]) > int(xx[i+1]):
                valid = False
    if valid: match+= 1

    if match == 2: count+=1

print('Part 1: %d' % count)

# part 2: 844 < ans < 1634
# not 906, 1122, 1407