r, c, zr, zc = [int(w) for w in input().split()]
for i in range(r):
    line = input()
    for j in range(zr):
        for c in line:
            print(c * zc, end='')
        print()