from math import acos
from math import asin
from math import atan
from math import sin
from math import cos
from math import pi

t = int(input())
l = 0
for i in range(t):
    a, b, c = [int(w) for w in input().split()]
    if a > b:
        a, b = b, a
    beta = acos((a*a + c*c - b*b) / 2 / a / c)
    alpha = acos((b*b + c*c - a*a) / 2 / b / c)
    h = b * sin(alpha)

    if beta > (pi / 2):
        p = a * cos(pi - beta)
        n = p + (c / 2)        
    else:
        m = a * cos(beta)
        n = (c / 2) - m
    theta = atan(n / h)
    l += (c * cos(theta))
print(l)