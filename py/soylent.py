from sys import stdin
print('\n'.join(str((int(w) + 399) // 400) for w in stdin.readlines()[1:]))