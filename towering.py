import itertools

nums = list((int(i) for i in input().split()))
h, t1, t2 = nums[:6], nums[6], nums[7]
h.sort()

for c in itertools.combinations(h, 3):
    if (sum(c) == t1):
        ordered = list(reversed(c))
        ordered.extend(box for box in reversed(h) if box not in c)
        print(' '.join(str(bh) for bh in ordered))
