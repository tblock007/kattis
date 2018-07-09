n = int(input())
for i in range(n):
    b, p = [float(w) for w in input().split()]
    print((b - 1) * 60.0 / p, 60.0 * b / p, (b + 1) * 60.0 / p)