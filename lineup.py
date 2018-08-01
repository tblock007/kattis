n = int(input())
ap = True
dp = True
prev = input()
for i in range(n - 1):
    curr = input()
    if (curr > prev):
        dp = False
    if (curr < prev):
        ap = False
    prev = curr
if (not ap) and (not dp):
    print('NEITHER')
elif ap:
    print('INCREASING')
else:
    print('DECREASING')