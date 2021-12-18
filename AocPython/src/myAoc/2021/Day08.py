"""
Each line of the input includes 10 7-character words separated by "|" from
4 words of variable length. The former represent each of the ten numerals
between 0 and 9, with the letters denoting the wires connected to the segments
of a 7-segment display that are turned on to show each numeral. The mapping of
wires to segments is unknown, and must be deduced by the program. The mapping of
wires to segments is specific to each row of input.

The words to the right of the "|" represent four number values displayed using
the mapping scheme that encodes the 10 numbers to the let of the "|".

Part 1: Determine the number of values to the right of the "|" that represent
numbers that are displayed using a unique number of segments, i.e. 1 (2 segments),
4 (4 segments), 7 (3 segments), and 8 (7 seconds).

Part 2: Deduce the mapping of wires to segments for each row of input and decode
the values to the right of the "|" as a 4-digit decimal number. Determine the sum
of all the decoded numbers.
"""

from collections import defaultdict
import sys

digitslist = []
valueslist = []

f = open('2021/data/day08')
for l in f.readlines():
    inp = l.split('|')
    digitslist.append(inp[0].split())
    valueslist.append(inp[1].split())

count = 0
for v in valueslist:
    for vv in v:
        if len(vv) == 2 or len(vv) == 3 or len(vv) == 4 or len(vv) == 7: count+= 1

print('Part 1: %d' % count)


# Map valus must be sorted ascending
char_map = {}
char_map[(1,3,4,5,6,7)] = 0
char_map[(5,7)] = 1
char_map[(1,2,3,5,6)] = 2
char_map[(1,2,3,5,7)] = 3
char_map[(2,4,5,7)] = 4
char_map[(1,2,3,4,7)] = 5
char_map[(1,2,3,4,6,7)] = 6
char_map[(1,5,7)] = 7
char_map[(1,2,3,4,5,6,7)] = 8
char_map[(1,2,3,4,5,7)] = 9

def map_digits(digits):
    """
        Segment numbers. Map each wire character to one of these
             1111
            4    5
            4    5
             2222
            6    7
            6    7
             3333

        Map of each number character to number of segments it includes
        Num Segments        Characters
        2:                  1
        3:                  7
        4:                  4
        7:                  8
        5:                  2, 3, 5
        6:                  6, 9, 0
    """
    d = defaultdict(list)
    for digit in digits:
        d[len(digit)].append("".join(sorted(digit)))

    s = {}
    # Segment 1: Wire that's in 7 (3 segments) and not in 1 (2 segments)
    s[1] = list(set(d[3][0]) - set(d[2][0]))[0]

    # The three character will be the only number with 5 segments that differs from the other 5-segment
    # numbers in one letter only
    if abs(len(set(d[5][0]) - set(d[5][1]))) == 1 and abs(len(set(d[5][0]) - set(d[5][2]))) == 1:
        c3 = d[5][0]
    elif abs(len(set(d[5][1]) - set(d[5][0]))) == 1 and abs(len(set(d[5][1]) - set(d[5][2]))) == 1:
        c3 = d[5][1]
    else:
        c3 = d[5][2]

    # Segment 2 is the wire that is in the three character and in the 4 character (4 segments), and not in the 1 character (2 segments)
    s[2] = list(set(c3).intersection(set(d[4][0])) - set(d[2][0]))[0]

    # Segement 4 is the wire that's in the 4 character (4 segments) and not in the 1 character (2 segments) and is not segment 2
    s[4] = list(set(d[4][0]) - set(d[2][0]) - set ([s[2]]))[0]

    # Five-segment numbers excluding 3 will be 2 and 5
    two_or_five = list(set(d[5]) - set([c3]))
    # The wires that differ will be segments 4, 5, 6, and 7
    diffs= (set(two_or_five[0]).union(set(two_or_five[1]))) - (set(two_or_five[0]).intersection(set(two_or_five[1])))

    # Segment 6 will be the wire that is not in 4 (4 segments) and not in 1 (2 segments)
    for c in diffs:
        if c not in d[2][0] and c not in d[4][0]:
            s[6] = c
            break

    # Segments 2, 5, and 6 will each not be in all six-segment numbers
    unique_in_sixes = set(d[6][0]).union(set(d[6][1])).union(set(d[6][2])) - \
        set(d[6][0]).intersection(set(d[6][1])).intersection(set(d[6][2]))

    # The wire that's also in 1 (2 segments) is segment 5
    s[5] = list(unique_in_sixes.intersection(set(d[2][0])))[0]

    # Segment 7 is the segment in 1 (2 segments) that is not segment 5
    s[7] = list(set(d[2][0]) - set(s[5]))[0]

    # The remaining wire is segment 3
    s[3] = list(set(list('abcdefg')) - set(s.values()))[0]

    # print(p)
    if len(set(s)) != 7:
        print("ERROR: Positions generated are not all unique")
        sys.exit()

    # Map each wire letter to the segment it was found to represent
    m = {}
    for i in range(1, 8):
        m[s[i]] = i

    return m



def decode_value(values, vmap):
    res= 0
    mult = 1000
    for digit in values:
        digit = tuple(sorted(map(lambda x: vmap[x], digit)))
        res+= (char_map[digit] * mult)
        mult/= 10
    return res


value = 0
for i in range(len(digitslist)):
    vmap = map_digits(digitslist[i])
    value+= decode_value(valueslist[i], vmap)

print('Part 2: %d' % value)

# Part 1: 387
# Part 2: 986034