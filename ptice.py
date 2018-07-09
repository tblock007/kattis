def score(ans, pat):
    result = 0
    for i in range(len(ans)):
        if (ans[i] == pat[i % len(pat)]):
            result = result + 1
    return result

n = int(input())
ans = input()
a = score(ans, 'ABC')
b = score(ans, 'BABC')
c = score(ans, 'CCAABB')
m = max(a, b, c)
print(m)
if (a == m):
    print('Adrian')
if (b == m):
    print('Bruno')
if (c == m):
    print('Goran')
