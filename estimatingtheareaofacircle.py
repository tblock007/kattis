import math
while True:
	r, m, c = [float(w) for w in input().split()]
	if (r == 0 and m == 0 and c == 0):
		break
	
	print('{0} {1}'.format(math.pi * r * r, c / m * r * r * 4.0))