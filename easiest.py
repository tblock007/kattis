def sd(n):
	sum = 0
	while (n > 0):
		sum = sum + (n % 10)
		n = n // 10
	return sum
	
while True:
	n = int(input())
	if (n == 0): break
	
	s = sd(n)
	m = 11
	while True:
		if (sd(n * m) == s):
			print(m)
			break
		m = m + 1