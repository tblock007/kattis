k = int(input())
n = int(input())
t = 0
for i in range(n):
    d, r = input().split()
    t = t + int(d)
    if (t > 210):
        print(k)
        break
    if (r == 'T'):
        k = (k % 8) + 1
