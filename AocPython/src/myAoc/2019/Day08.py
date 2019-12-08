w = 25
h = 6

layers = []
f = open('2019/data/day08')
data = f.readline()
data = data.strip()
for i in range(0, len(data), w*h):
    layers.append(data[i:i+w*h])

zeroes = {}
i = 0
for layer in layers:
    zeroes[i] = layer.count('0')
    i+= 1

min_layer = (int(1e12), int(1e12))
for k, v in zeroes.items():
    if v < min_layer[1]:
        min_layer = (k,v)

print('Part 1: %d' % (layers[min_layer[0]].count('1') * layers[min_layer[0]].count('2')))

print('Part 2')
for i in range(h):
    row = ''
    for j in range(w):
        for layer in layers:
            px = layer[i*w + j]
            if px == '2':
                continue
            break
        row+= ('  ' if px == '2' or px == '0' else ' #')
    print(row)
