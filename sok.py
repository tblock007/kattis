have = [int(w) for w in input().split()]
parts = [int(w) for w in input().split()]
ratio = min(p[0] / p[1] for p in zip(have, parts))
rem = [str(have[i] - parts[i] * ratio) for i in range(3)]
print(' '.join(rem))
