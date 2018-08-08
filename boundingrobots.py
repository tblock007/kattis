def move(a, b, dir, d, w, l):
    if dir == "u":
        b = (b + d if (b + d <= l) else l)
    elif dir == "d":
        b = (b - d if (b - d >= 0) else 0)
    elif dir == "l":
        a = (a - d if (a - d >= 0) else 0)
    elif dir == "r":
        a = (a + d if (a + d <= w) else w)
    return (a, b)

def track(a, b, dir, d):
    if dir == "u":
        b = b + d
    elif dir == "d":
        b = b - d
    elif dir == "l":
        a = a - d
    elif dir == "r":
        a = a + d
    return (a, b)


while True:
    w, l = [int(w) - 1 for w in input().split()]
    if w == -1 and l == -1:
        break
    n = int(input())
    x, y = 0, 0
    xt, yt = 0, 0
    for i in range(n):
        tokens = input().split()
        x, y = move(x, y, tokens[0], int(tokens[1]), w, l)
        xt, yt = track(xt, yt, tokens[0], int(tokens[1]))
    print('Robot thinks {0} {1}'.format(xt, yt))
    print('Actually at {0} {1}'.format(x, y))
    print()