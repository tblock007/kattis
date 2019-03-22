line = input()
w, l, u, s = 0, 0, 0, 0
for c in line:
	if c == '_': w = w + 1
	elif c.islower(): l = l + 1
	elif c.isupper(): u = u + 1
	else: s = s + 1
print(w / len(line))
print(l / len(line))
print(u / len(line))
print(s / len(line))