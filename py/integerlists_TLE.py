# Judged at TLE (>1.00s)

def printlist(l):
    if len(l) == 0:
        return '[]'
    else:
        result = '['
        result += str(l[0])
        for i in range(1, len(l)):
            result += ',{0}'.format(l[i])
        result += ']'
        return result

def solve(p, x):
    for c in p:
        if c == 'R':
            x.reverse()
        if c == 'D':
            if len(x) == 0:
                return 'error'
            else:
                x = x[1:]

    return printlist(x)

t = int(input())
for _ in range(t):
    p, n, l = input(), int(input()), input()[1:-1]
    if l == "":
        x = []
    else:
        x = [int(w) for w in l.split(',')]
    
    print(solve(p, x))
    
