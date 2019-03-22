t = int(input())
for cas in range(t):
    r, c = [int(w) for w in input().split()]
    grid = [[int(w) for w in list(input())] for i in range(r)]
    rc, cc = set(), set()
    count = 0
    for i in range(r):
        for j in range(c):
            if (grid[i][j] == 1):
                rc.add(i)
                cc.add(j)
                count = count + 1
    if count == len(rc) * len(cc):
        if (len(rc) == 1 or len(cc) == 1):
            rep = 'P'
        else:
            rep = 'I'
        output = [[rep if grid[i][j] == 1 else 'N' for j in range(c)] for i in range(r)]
        for ii in range(r):
            print(''.join(output[ii]))
    else:
        print('impossible')  
    print('----------')