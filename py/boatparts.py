import sys
p, n = [int(w) for w in input().split()]
parts = set()
for i in range(n):
    parts.add(input())
    if (len(parts) == p):
        print(i + 1)
        sys.exit()
if (len(parts) < p):
    print('paradox avoided')
