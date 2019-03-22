from sys import stdin
import math
cas = 1
for line in stdin.readlines():
    e, m = [int(w) for w in line.split()]
    offset = (e - m) % 687
    a = (offset * 32) % 687
    print('Case {0}: {1}'.format(cas, 365 * a - e))
    cas += 1
