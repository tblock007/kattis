import math

n, w, h = [int(t) for t in input().split()]
d = math.sqrt(w*w + h*h)
for i in range(n):
    l = int(input())
    print('DA' if (l <= d) else 'NE')