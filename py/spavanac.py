h, m = [int(w) for w in input().split()]
if m >= 45:
    m = m - 45
else:
    m = m + 15
    h = (h + 23) % 24
print('{0} {1}'.format(h, m))