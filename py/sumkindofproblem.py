n = int(input())
for i in range(n):
    k = int(input().split()[1])
    tri = k * (k + 1) / 2
    print(i + 1, round(tri), round((tri * 2) - k), round(tri * 2))