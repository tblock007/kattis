n = int(input())
a = list(map(int, input().split()))

total = 0
threshold = a[-1]
for i in range(len(a) - 2, -1, -1):
    if a[i] >= threshold:
        total += a[i] - (threshold - 1)
        threshold -= 1
    else:
        threshold = a[i]

if threshold < 0:
    print(1)
else:
    print(total)