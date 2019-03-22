def get_unique(c):
    c.sort()
    avg = sum(c) / 3.0
    eavg = (c[0] + c[2]) / 2.0
    if (eavg < avg):
        return c[0]
    else:
        return c[2]

x, y = [], []
for i in range(3):
    a, b = [int(num) for num in input().split()]
    x.append(a)
    y.append(b)
print('{0} {1}'.format(get_unique(x), get_unique(y)))
