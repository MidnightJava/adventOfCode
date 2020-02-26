def deal_newStack(cards):
    return cards[::-1]

def cut(cards, n):
    return cards[n:] + cards[:n]

def deal_incr(cards, n):
    new_cards = list(map(lambda x: None, cards))
    idx = 0
    for i in range(len(cards)):
        new_cards[idx] = cards[i]
        idx = (idx + n) % len(cards)
    return new_cards

cards = [i for i in range(10007)]

f = open('2019/data/day22')
count = 0
for line in f.read().split('\n'):
    if line.startswith('cut'):
        cards = cut(cards, int(line.split()[1]))
    elif line.startswith('deal with'):
        cards = deal_incr(cards, int(line.split()[3]))
    elif line.startswith('deal into'):
        cards = deal_newStack(cards)
    else:
        print('Failed to parse line %s' % line)
    count+= 1

print('Part 1', cards.index(2019))

#P art 1: 4086