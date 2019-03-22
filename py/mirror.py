t = int(input())
for i in range(t):
    print('Test {0}'.format(i + 1))
    r, c = [int(w) for w in input().split()]
    grid = [list(input()) for i in range(r)]
    for j in range(r):
        row = r - j - 1
        print(''.join(reversed(grid[row])))