e, f, c = [int(w) for w in input().split()]
b, t = e + f, 0
while b >= c:
    t = t + (b // c)
    b = (b % c) + (b // c)
print(t)