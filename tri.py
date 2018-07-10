def solve(a, b, c):
    op = ['+', '-', '*', '/']
    for o in op:
        if eval(str(b) + o + str(c)) == a:
            return '{0}={1}{2}{3}'.format(a, b, o, c)
    for o in op:
        if eval(str(a) + o + str(b)) == c:
            return '{0}{1}{2}={3}'.format(a, o, b, c)

a, b, c = [int(w) for w in input().split()]
print(solve(a, b, c))