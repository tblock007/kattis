import sys
for line in sys.stdin.readlines():
    n, d = [int(w) for w in line.split()]
    if n != 0 or d != 0:
        print('{0} {1} / {2}'.format(n // d, n % d, d))