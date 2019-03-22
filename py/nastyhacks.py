n = int(input())
for i in range(n):
    r, e, c = [int(t) for t in input().split()]
    if (e - c > r):
        print('advertise')
    elif (e - c < r):
        print('do not advertise')
    else:
        print('does not matter')