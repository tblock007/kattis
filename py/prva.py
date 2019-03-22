def word(grid, a, b, down):
    i, j = a, b
    result = []
    if down:
        while i < len(grid) and grid[i][j] != '#':
            result.append(grid[i][j])
            i = i + 1
    else:
        while j < len(grid[i]) and grid[i][j] != '#':
            result.append(grid[i][j])
            j = j + 1            
    return ''.join(result)


r, c = [int(w) for w in input().split()]
grid = [list(input()) for i in range(r)]
mins = 'z' * r * c
for i in range(r):
    for j in range(c):
        if (grid[i][j] != '#'):
            if (i == 0 or grid[i - 1][j] == '#'):
                cand = word(grid, i, j, True)
                if (len(cand) > 1):
                    mins = min(mins, cand)
            if (j == 0 or grid[i][j - 1] == '#'):
                cand = word(grid, i, j, False)
                if (len(cand) > 1):
                    mins = min(mins, cand)
print(mins)
