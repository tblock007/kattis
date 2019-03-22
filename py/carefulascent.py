x, y = [float(w) for w in input().split()]
n = int(input())
ty = y
for i in range(n):
    l, u, f = [float(w) for w in input().split()]
    ty -= (1.0 - f) * (u - l)
print(x / ty)