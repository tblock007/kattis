n, p, k = map(int, input().split())
t = [0] + [int(w) for w in input().split()] + [k]
diffs = [(t[i] - t[i - 1]) for i in range(1, len(t))]
factors = [(100 + p * e) / 100.0 for e in range(len(diffs))]
print(sum(diffs[i] * factors[i] for i in range(len(diffs))))