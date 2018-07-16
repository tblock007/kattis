import math
while True:
    a, b, s, m, n = [int(w) for w in input().split()]
    if (a == 0 and b == 0 and s == 0 and m == 0 and n == 0): break
    x, y = a * m, b * n
    print('{0:.2f} {1:.2f}'.format(math.atan(y / x) * 180.0 / math.pi, math.sqrt(x**2 + y**2) / s))