line = input()
t, c, g = line.count('T'), line.count('C'), line.count('G')
print((7 * min(t, c, g)) + t**2 + c**2 + g**2)