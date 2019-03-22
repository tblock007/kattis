def ina(grid, i, j):
    dr = [-2, -2, -1, -1, 1, 1, 2, 2]
    dc = [-1, 1, -2, 2, -2, 2, -1, 1]
    for ii in range(len(dr)):
        if (i + dr[ii] >= 0) and (i + dr[ii] <= 4) and (j + dc[ii] >= 0) and (j + dc[ii] <= 4):
            if grid[i + dr[ii]][j + dc[ii]] == 'k':
                return False
    return True

grid = [list(input()) for i in range(5)]
clean = True
count = 0
for i in range(5):
    for j in range(5):
        if (grid[i][j] == 'k'):
            count = count + 1
            if not ina(grid, i, j):
                clean = False
print('valid' if clean and count == 9 else 'invalid')