def advance(s, i):
    if s[i] == 'L':
        return (False, i + 1)
    i += 1
    while (i < len(s) and s[i] == 'L'):
        i += 1
    return (True, i)

n = int(input())
s = 'R' + input()
order = [i + 1 for i in range(n)]
i = 0
while i < len(s):
    flag, j = advance(s, i)
    order[i:j] = reversed(order[i:j])
    i = j
for o in order:
    print(o)

