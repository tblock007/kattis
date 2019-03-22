import math
n = int(input())
for i in range(n):
    x, y = [int(w) for w in input().split()]
    h = (x + y - math.sqrt(x*x - x*y + y*y)) / 6.0
    print(h * (y - 2 * h) * (x - 2 * h))