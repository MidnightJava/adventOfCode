'''
Created on Dec 14, 2016

@author: maleone
'''
rows, cols = 8, 11

tx = 7
ty = 4

matrix = []

def isWall(x, y):
    a = x*x + 3*x + 2*x*y + y + y*y + 10
    b = bin(a)
    numBits = b.count("1")
    return True if numBits % 2 != 0 else False

for y in xrange(rows):
    row = list()
    for x in xrange(cols):
        row.append(1 if not isWall(x, y) else 0)
    matrix.append(row)


def traverse_matrix(A, directions, i, j, visited):
    global rows, cols, tx, ty
    def can_we_proceed(A, row, col, visited, current):
        return (row >=0 and row < ty and col >=0 and col < tx and \
                not visited[row][col] and (current == A[row][col]) and A[row][col] == 1)

    visited[i][j] = True
    for k in range(len(directions)):
        if can_we_proceed(A, i+directions[k][0], j+directions[k][1], visited, A[i][j]):
            print "({0},{1})".format(i+directions[k][0],j+directions[k][1])
            traverse_matrix(A, directions, i+directions[k][0], j+directions[k][1], visited)

def solve(matrix):
    global rows, cols
    rows, cols = len(matrix) , len(matrix[0])
    if (rows == 1 or cols == 1):
        return 1
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = []
    for i in range(rows):
        l = []
        for j in range(cols):
            l.append(False)
        visited.append(l)

    tup1 = ();
    for i in range(1, tx+1):
        for j in range(1, ty+1):
            tup1 = (i,j);
            if not visited[i][j]:
                traverse_matrix(matrix, directions, i, j, visited)   
#                 print "Traversed {0};".format(tup1)
solve(matrix)