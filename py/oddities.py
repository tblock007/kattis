n = int(input())
for _ in range(n):
	x = int(input())
	print('{0} is {1}'.format(x, 'even' if x % 2 == 0 else 'odd'))
