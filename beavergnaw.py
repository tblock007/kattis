import math

while True:
    D, V = [int(w) for w in input().split()]
    if (D == 0 and V == 0):
        break

    s = D**3.0 - (6.0 * V / math.pi)
    print(s ** (1.0/3.0))