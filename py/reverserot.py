from sys import stdin

def conv(ch, sh, l):
    if ch == '_':
        i = 26
    elif ch == '.':
        i = 27
    else:
        i = ord(ch) - ord('A')
    i = (i + sh) % 28
    return l[i]

c = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ_.')
for line in stdin.readlines()[:-1]:
    s, st = line.split()
    result = reversed([conv(ch, int(s), c) for ch in st])
    print(''.join(result))
