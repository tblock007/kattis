r, c = [int(w) for w in input().split()]
grid = [list(input()) for i in range(r)]

sq = [0] * 5
for i in range(r - 1):
    for j in range(c - 1):
        cars = 0
        buildings = 0
        if grid[i][j] == 'X': cars = cars + 1
        if grid[i][j] == '#': buildings = buildings + 1
        if grid[i + 1][j] == 'X': cars = cars + 1
        if grid[i + 1][j] == '#': buildings = buildings + 1
        if grid[i][j + 1] == 'X': cars = cars + 1
        if grid[i][j + 1] == '#': buildings = buildings + 1
        if grid[i + 1][j + 1] == 'X': cars = cars + 1
        if grid[i + 1][j + 1] == '#': buildings = buildings + 1
        if buildings == 0:
            sq[cars] = sq[cars] + 1
for s in sq:
    print(s)