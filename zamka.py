def sd(x):
    sum = 0
    while x > 0:
        sum = sum + (x % 10)
        x = x // 10
    return sum

import sys
l,d,x = [int(line) for line in sys.stdin.readlines()]
for i in range(l, d + 1):    
    if (sd(i) == x):
        print(i)
        break
for i in range(d, l - 1, -1):
    if (sd(i) == x):
        print(i)
        break