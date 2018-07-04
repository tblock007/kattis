import math
h, v = [int(w) for w in input().split()]
print(math.ceil(h / math.sin(v * math.pi / 180.0)))