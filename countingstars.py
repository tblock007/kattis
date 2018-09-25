import sys

def ff(grid, i, j, d):
    if (grid[i][j] != '-'):
        return False

    grid[i][j] = d
    if (i > 0 and grid[i-1][j] == '-'):
        ff(grid, i-1, j, d)
    if (i < len(grid) - 1 and grid[i+1][j] == '-'):
        ff(grid, i+1, j, d)
    if (j > 0 and grid[i][j-1] == '-'):
        ff(grid, i, j-1, d)
    if (j < len(grid[0]) - 1 and grid[i][j+1] == '-'):
        ff(grid, i, j+1, d)
    return True

sys.setrecursionlimit(100000)
cas = 1
while True:
    try:
        m, n = [int(w) for w in input().split()]
    except:
        break
    grid = [(list(input())) for i in range(m)]

    count = 0
    for i in range(m):
        for j in range(n):
            if ff(grid, i, j, 'o'):
                count += 1
    print('Case {0}: {1}'.format(cas, count))
    cas += 1