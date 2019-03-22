import sys
s = set(int(w) % 42 for w in sys.stdin.readlines())
print(len(s))