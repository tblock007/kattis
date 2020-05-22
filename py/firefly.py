from bisect import bisect_left, bisect_right
from collections import Counter

def stalags(level):
    global u
    return len(u) - bisect_left(u, level)

def stalacs(level):
    global d, h
    return len(d) - bisect_left(d, h - level + 1)

def stals(level):
    return stalags(level) + stalacs(level)


n, h = [int(w) for w in input().split()]
u, d = [], []
for i in range(n):
    if i % 2 == 0:
        u.append(int(input()))
    else:
        d.append(int(input()))
u.sort()
d.sort()

c = Counter()
for level in range(1, h + 1):
    c[stals(level)] += 1
least = min(c.keys())
print(least, c[least])
