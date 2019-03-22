import math

def decode(s):
	n = int(math.sqrt(len(s)) + 1.0e-11)
	for i in range(n - 1, -1, -1):
		for j in range(i, len(s), n):
			print(s[j], end='')
	print()
	
n = int(input())
for i in range(n):
	message = input()
	decode(message)