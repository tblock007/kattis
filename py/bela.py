import sys

def val(c, dom):
    if dom:
        if c == 'A': return 11
        if c == 'K': return 4
        if c == 'Q': return 3
        if c == 'J': return 20
        if c == 'T': return 10
        if c == '9': return 14
        if c == '8': return 0
        if c == '7': return 0
    if not dom:
        if c == 'A': return 11
        if c == 'K': return 4
        if c == 'Q': return 3
        if c == 'J': return 2
        if c == 'T': return 10
        if c == '9': return 0
        if c == '8': return 0
        if c == '7': return 0

n, dominant = [w for w in sys.stdin.readline().split()]
print(sum([val(h[0], h[1] == dominant) for h in sys.stdin.readlines()]))