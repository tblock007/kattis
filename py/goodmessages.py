def offset(c, o):
    i = ord(c) - ord('a') + o
    i = i % 26
    return chr(i + ord('a'))

def transform(s, o):
    return ''.join(offset(c, o) for c in s)

def annoying(s):
    v = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') + s.count('y')
    c = len(s) - v
    if (2 * v >= c):
        return True
    return False

o, s, n = int(input()), input(), int(input())
good, bad = 0, 0
for _ in range(n):
    s = transform(s, o)
    if (annoying(s)):
        bad += 1
    else:
        good += 1

if good > bad:
    print('Boris')
else:
print('Colleague')