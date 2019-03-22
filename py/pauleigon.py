n, q, p = [int(w) for w in input().split()]
r = (q + p) // n
if (r % 2 == 0):
    print('paul')
else:
    print('opponent')