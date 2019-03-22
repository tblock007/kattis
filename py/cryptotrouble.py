def zss(digits):
    zc = digits.count(0)
    return pow(2, zc, 1000000007) # covers the empty subset

n = int(input())
s = [int(c) for c in input()]

sswm = [[-1 for i in range(n)] for j in range(3)]
sswm[0][0] = 1 + (1 if s[0] % 3 == 0 else 0)
sswm[1][0] = (1 if s[0] % 3 == 1 else 0)
sswm[2][0] = (1 if s[0] % 3 == 2 else 0)

for i in range(1, n):
    sswm[0][i] = ((sswm[(3 - (s[i] % 3)) % 3][i - 1]) + (sswm[0][i - 1])) % 1000000007
    sswm[1][i] = ((sswm[(4 - (s[i] % 3)) % 3][i - 1]) + (sswm[1][i - 1])) % 1000000007
    sswm[2][i] = ((sswm[(5 - (s[i] % 3)) % 3][i - 1]) + (sswm[2][i - 1])) % 1000000007

print((sswm[0][n - 1] - zss(s) + 1000000007) % 1000000007)

