line = input()
substrings = set()
for i in range(len(line) - 1):
    for j in range(i + 1, len(line)):
        substrings.add(line[i:j + 1])
best = len(line)
for ss in substrings:
    count = len(ss) + len(line.replace(ss, 'M'))
    best = min(best, count)
print(best)
