c, k = [int(t) for t in input().split()]
if k == 1 and c == 0:
    print('ALL GOOD')
elif k == 1:
    print('IMPOSSIBLE')
else:
    print(c / (1 - k))