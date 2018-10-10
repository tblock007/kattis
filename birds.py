import sys
import math

def cb(l, d):
    return math.floor((l / d) + 1e-12) + 1

lines = sys.stdin.readlines()
l, d, n = [int(w) for w in lines[0].split()]
l -= 12
birds = list(sorted(int(bird) - 6 for bird in lines[1:]))
if len(birds) == 0:
    print(cb(l, d))
else:
    result = cb(birds[0], d) + cb(l - birds[-1], d) - 2
    for i in range(1, len(birds)):
        result += (cb(birds[i] - birds[i - 1], d)) - 2
print(result)