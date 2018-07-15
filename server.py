import sys

n, t = [int(w) for w in input().split()]
tasks = [int(w) for w in input().split()]
total = 0
for i in range(n):
    total = total + tasks[i]
    if (total > t):
        print(i)
        sys.exit()
print(n)