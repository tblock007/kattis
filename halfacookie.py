from sys import stdin
import math

for line in stdin.readlines():
    r, x, y = [float(w) for w in line.split()]
    if (x*x + y*y <= r*r):
        d = math.hypot(x, y)
        l = 2 * (math.sqrt(r*r - d*d))
        theta = math.acos(1 - (l*l / 2 / r/r))
        acircle = math.pi * r * r
        asector = acircle * theta / (2 * math.pi)
        atri = d * l / 2
        asegment = asector - atri
        print(acircle - asegment, asegment)
    else:
        print('miss')