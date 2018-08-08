import math

n = int(input())
r = [int(w) for w in input().split()]
for i in range(1, n):
    print('{0}/{1}'.format(int(r[0] / math.gcd(r[0], r[i])), int(r[i] / math.gcd(r[0], r[i]))))