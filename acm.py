p, s = 0, 0
inc = {}
while True:
    comp = input().split()
    if len(comp) == 1: break
    m, prob, j = int(comp[0]), comp[1], comp[2]
    if j == 'right':
        p = p + 1
        s = s + m + inc.get(comp[1], 0) * 20
    elif j == 'wrong':
        inc[comp[1]] = inc.get(comp[1], 0) + 1
print(p, s)