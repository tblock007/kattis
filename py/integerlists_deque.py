# Judged at 0.28s

from collections import deque


def dequeToString(x, rev):
    if len(x) == 0:
        return '[]'
    if rev:
        result = '[{0}'.format(x.pop())
        while x:
            result += ',{0}'.format(x.pop())
    else:
        result = '[{0}'.format(x.popleft())
        while x:
            result += ',{0}'.format(x.popleft())
    result += ']'
    return result


def solve(program, x):
    rev = False
    for c in program:
        if c == 'R':
            rev = not rev
        if c == 'D':
            if len(x) == 0:
                return 'error'

            if rev:
                x.pop()
            else:
                x.popleft()

    return dequeToString(x, rev)
    

t = int(input())
for _ in range(t):
    program, n, line = input(), int(input()), input()[1:-1]
    if line == "":
        x = deque()
    else:
        x = deque(int(w) for w in line.split(','))
    
    print(solve(program, x))
    
