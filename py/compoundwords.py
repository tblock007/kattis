from sys import stdin
words = [w for l in stdin.readlines() for w in l.split()]
print(*sorted(set(a + b for a in words for b in words if a != b)), sep='\n')