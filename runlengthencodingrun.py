def ed(inst, ss):
    if inst == 'E':
        return ss[0] + str(len(ss))
    else:
        return ss[0] * int(ss[1:])

inst, s = input().split()
ans = ''
if inst == 'E':
    i, j = 0, 0
    while j < len(s):
        while j < len(s) and s[j] == s[i]:
            j += 1
        ans += ed(inst, s[i:j])
        i = j
if inst == 'D':
    for i in range(0, len(s), 2):
        ans += ed(inst, s[i:i + 2])
print(ans)
