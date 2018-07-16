n = int(input())
for i in range(n):
    s, ropes, reds, blues = int(input()), input().split(), [], []
    for r in ropes:
        if r[-1] == 'R':
            reds.append(int(r[:-1]))
        elif r[-1] == 'B':
            blues.append(int(r[:-1]))
    reds = sorted(reds, reverse = True)
    blues = sorted(blues, reverse = True)
    segs = min(len(reds), len(blues))
    print('Case #{0}: {1}'.format(i + 1, sum(sum(p) for p in zip(reds[0:segs], blues[0:segs])) - (2 * segs)))
    