def sidel(n):
    num = 0
    s = 2
    while num < n:
        yield s
        s = (2 * s - 1)
        num += 1

ans = [i * i for i in sidel(16)]
n = int(input())
print(ans[n])