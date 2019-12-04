count = 0

for x in range(134564, 585159+1):
    match = 0
    xx = str(x)
    valid = False
    for i in range(len(xx)):
        if i < len(xx)-1 and xx[i] == xx[i+1]:
          valid = True
    if valid: match+= 1

    # mc = 0
    # for i in range(len(xx)):
    #     if i < len(xx)-1 and xx[i] == xx[i+1]:
    #         mc+= 1

    valid = True
    for i in range(len(xx)):
        if i < len(xx)-1:
            if int(xx[i]) > int(xx[i+1]):
                valid = False
    if valid: match+= 1

    if match == 2: count+=1

print('Part 1: %d' % count)

# part 2 < 1634
