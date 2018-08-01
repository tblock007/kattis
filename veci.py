import sys

x = list(input())
loi = len(x) - 1
while loi >= 1:
    if (x[loi - 1] < x[loi]):
        break
    loi = loi - 1
if loi == 0:
    print('0')
else:
    loi = loi - 1
    ni = len(x) - 1
    while ni >= 0:
        if (x[ni] > x[loi]):
            break
        ni = ni - 1
    tbr = x[loi + 1:ni] + x[loi:loi + 1] + x[ni + 1:]
    tbr.reverse()
    result = x[:loi] + x[ni:ni + 1] + tbr
    print(''.join(result))