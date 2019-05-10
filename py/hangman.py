rem, order = set(input()), input()
h = 0
for c in order:
	if c in rem:
		rem.remove(c)
		if len(rem) == 0:
			print('WIN')
			break
	else:
		h += 1
		if h == 10:
			print('LOSE')
			break
