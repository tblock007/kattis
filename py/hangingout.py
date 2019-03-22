l, x = [int(w) for w in input().split()]
curr = 0
count = 0
for i in range(x):
    inst, num = input().split()
    if (inst == 'enter'):
        if (curr + int(num) > l):
            count = count + 1
        else:
            curr = curr + int(num)
    if (inst == 'leave'):
        curr = curr - int(num)
print(count)