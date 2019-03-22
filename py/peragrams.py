chars = list(input())
counts = {}
for c in chars:
    if c in counts.keys():
        counts[c] += 1
    else:
        counts[c] = 1
oddcounts = 0
for count in counts.values():
    if count % 2 == 1:
        oddcounts += 1
print(oddcounts - 1 if oddcounts >= 1 else 0)