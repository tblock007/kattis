import math
a, b, l = [int(w) for w in input().split()]
print('yes' if (a * b / math.gcd(a, b) <= l) else 'no')