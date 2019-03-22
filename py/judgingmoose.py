l, r = [int(w) for w in input().split()]
print('Not a moose' if (l + r == 0) else ('{0} {1}'.format(('Odd' if (l != r) else 'Even'), 2 * max(l, r))))