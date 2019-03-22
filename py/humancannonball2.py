import math

n = int(input())
for i in range(n):
	v, a, x, h1, h2 = [float(w) for w in input().split()]
	t = x / v / math.cos(a * math.pi / 180.0)
	y = v * t * math.sin(a * math.pi / 180.0) - 0.5 * 9.81 * t * t
	print('Safe' if (y - 1 >= h1 and y + 1 <= h2) else 'Not Safe')