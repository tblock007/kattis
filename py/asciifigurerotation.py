cas = 1
while True:
    n = int(input())
    if n == 0: break

    lines = []
    for i in range(n):
        lines.append(input())
    maxlen = max(len(l) for l in lines)
    padded = [l + (' ' * (maxlen - len(l))) for l in lines]
    rotated = [[padded[j][i] for j in range(len(padded) - 1, -1, -1)] for i in range(maxlen)]

    if cas > 1:
        print()
    for s in rotated:
        print(''.join(s).rstrip().replace('|','*').replace('-','|').replace('*','-'))
    cas = cas + 1