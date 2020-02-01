import os

# ASCII Escape codes
RED = u'\u001b[31;1m'
BLUE = u'\u001b[34;1m'
GREEN = u'\u001b[32;1m'
UNDERLINE =u'\u001b[4m'
BOLD = u'\u001b[1m'
REVERSED = u'\u001b[7m'
RST = u'\u001b[0m'

h, w = os.popen('stty size', 'r').read().split()
y0 = int(h) - 18

def print_at_pos(s, coord):
    y,x = coord
    print('\033[%d;%dH%s' % (y,x,s))

pos_map = [
    (y0, 0), (y0, 50),
    (y0+2, 0), (y0+2, 50),
    (y0+4, 0), (y0+4, 50),
    (y0+6, 0), (y0+6, 50),
    (y0+8, 0), (y0+8, 50),
    (y0+10, 0), (y0+10, 50),
    (y0+12, 0), (y0+12, 50)
]

print('\033[2J')
print_at_pos('Wrapper Test Client', (y0-4, 0))
print_at_pos("Status: %sConnected to wrapper service at http://localhost:320000%s" % (GREEN, RST), (y0-3, 0))


# print('%d x %d' % (int(rows), int(columns)))
print_at_pos('%sSwitches%s' % (UNDERLINE + BOLD, RST), pos_map[0])
print_at_pos('%sArgs%s' % (UNDERLINE + BOLD, RST), pos_map[1])
while True:
    for i in range(2, len(pos_map)):
       print_at_pos('Line %d' % i, pos_map[i])
    print_at_pos('Result: %sXXXX%s' % (RED, RST), (pos_map[-1][0] +2, 0))
    num = raw_input("\033[%d;%dHEnter a value: " % (pos_map[-1][0] +3, 0))
    print_at_pos(' '*50, (pos_map[-1][0] +3, 0))
    raw_input("\033[%d;%dHEnter another value: " % (pos_map[-1][0] +3, 0))
    print_at_pos(' '*50, (pos_map[-1][0] +3, 0))