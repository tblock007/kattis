from bisect import bisect_left

def is_valid(h):
    global p
    i = bisect_left(p, h)
    return (len(p) - i) >= h

n = int(input())
p = []
for _ in range(n):
    p.append(int(input()))
p.sort()

low = 0
high = 1000000000
while low <= high:
    mid = (low + high) // 2
    if (is_valid(mid) and not is_valid(mid + 1)):
        print(mid)
        break

    if (is_valid(mid)):
        low = mid + 1
    else:
        high = mid - 1