n, m = [int(w) for w in input().split()]
starts = []
ends = []
for _ in range(n):
    a, s = [int(w) for w in input().split()]
    starts.append(a)
    ends.append(a + s)
starts.sort()
ends.sort()

next_end = 0
count = 0
for start in starts:
    while ends[next_end] + m < start:
        next_end += 1
    if ends[next_end] <= start:
        count += 1
        next_end += 1
print(count)