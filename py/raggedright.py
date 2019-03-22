from sys import stdin
l = [len(line.strip()) for line in stdin.readlines()]
m = max(l)
print(sum((m - ll) ** 2 for ll in l[:-1]))