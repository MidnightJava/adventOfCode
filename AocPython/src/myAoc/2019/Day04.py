answers = []
for part in[0, 1]:
    count = 0
    for x in range(134564, 585159+1):
        match = 0
        xx = str(x)
        valid = False
        for i in range(len(xx)):
            if i < len(xx)-1:
                if xx[i] == xx[i+1]:
                    if part == 1:
                        if i < len(xx) - 2:
                            if xx[i] != xx[i+2] and xx[i] != xx[i-1]: valid = True
                        elif xx[i] != xx[i-1]: valid = True
                    else:
                        valid = True
        if valid or xx[-1] == xx[-2] and xx[-3] != xx[-1]: match+=1

        valid = True
        for i in range(len(xx)):
            if i < len(xx)-1:
                if int(xx[i]) > int(xx[i+1]):
                    valid = False
        if valid: match+= 1

        if match == 2: count+=1
    answers.append(count)

print('Part 1: %d' % answers[0])
print('Part 2: %d' % answers[1])

# Part 1: 1929
# Part 2: 1306