def offset(zoom, quad):
    factor = 2 ** (zoom - 1)
    if quad == '0':
        x, y = 0, 0
    elif quad == '1':
        x, y = 1, 0
    elif quad == '2':
        x, y = 0, 1
    elif quad == '3':
        x, y = 1, 1
    return factor * x, factor * y 

qk = input()
x, y = 0, 0
for i in range(len(qk)):
    x = x + offset(len(qk) - i, qk[i])[0]
    y = y + offset(len(qk) - i, qk[i])[1]
print(len(qk), x, y)