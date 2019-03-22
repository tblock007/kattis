n = int(input())
cups = []
for i in range(n):
	cup = input().split()
	if (cup[0].isdigit()):
		cup[0] = float(cup[0]) / 2.0
	else:
		cup[0],cup[1] = float(cup[1]),cup[0]
	cups.append(cup)
cups.sort(key = lambda l: l[0])
for c in cups:
	print(c[1])