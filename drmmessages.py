def rv(s):
	return sum(ord(i) - ord('A') for i in s)
	
def rot(c, n):
	return chr((((ord(c) - ord('A')) + n) % 26) + ord('A'))

line = input()
l1, l2 = line[:round(len(line) / 2)], line[round(len(line) / 2):]
rv1, rv2 = rv(l1), rv(l2)
rl1, rl2 = ''.join(rot(c, rv1) for c in l1), ''.join(rot(c, rv2) for c in l2)
print(''.join(rot(p[0], ord(p[1]) - ord('A')) for p in zip(rl1, rl2)))
