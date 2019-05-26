n, q = [int(w) for w in input().split()]
c = [int(w) for w in input().split()]
for _ in range(q):
	command, a, b = [int(w) for w in input().split()]
	if command == 1:
		c[a - 1] = b
	elif command == 2:
		print(abs(c[a - 1] - c[b - 1]))
