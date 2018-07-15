n = int(input())
mt, st = 0, 0
for i in range(n):
    m, s = [int(w) for w in input().split()]
    mt, st = mt + m, st + s
ans = st / mt / 60.0
print(ans if (ans > 1.0) else 'measurement error')