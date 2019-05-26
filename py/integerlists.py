# Judged at 0.21s

def printlist(x, dropFront, dropBack, rev):
    if dropFront + dropBack > len(x):
        return 'error'
    elif dropFront + dropBack == len(x):
        return '[]'
    else:
        if rev:
            return '[{0}]'.format(','.join(str(w) for w in reversed(x[dropFront:len(x) - dropBack])))
        else:
            return '[{0}]'.format(','.join(str(w) for w in x[dropFront:len(x) - dropBack]))


def solve(program, x):
    dropFront, dropBack = 0, 0
    rev = False
    for c in program:
        if c == 'R':
            rev = not rev
        if c == 'D':
            if rev:
                dropBack += 1
            else:
                dropFront += 1

    return printlist(x, dropFront, dropBack, rev)
    

t = int(input())
for _ in range(t):
    program, n, line = input(), int(input()), input()[1:-1]
    if line == "":
        x = []
    else:
        x = [int(w) for w in line.split(',')]
    
    print(solve(program, x))
    
