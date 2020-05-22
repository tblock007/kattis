from bisect import bisect_left

n, m = [int(w) for w in input().split()]
s, c = [], []
for _ in range(n):
    s.append(int(input()))
for _ in range(m):
    c.append(int(input()))
s.sort()
c.sort()

result = 0
for can in c:
    i = bisect_left(s, can)
    result += s[i] - can
print(result)
