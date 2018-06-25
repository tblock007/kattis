op = ['+','-','*','//']

d = {}
for a in range(4):
    for b in range(4):
        for c in range(4):
            expr = '4 ' + op[a] + ' 4 ' + op[b] + ' 4 ' + op[c] + ' 4'
            res = eval(expr)
            d[res] = expr + ' = ' + str(res)

n = int(input())
for i in range(n):
    q = int(input())
    if (q in d.keys()):
        print(d[q].replace('//', '/'))
    else:
        print('no solution')
