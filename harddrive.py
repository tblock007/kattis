n, c, b = [int(w) for w in input().split()]
broken = set((int(w) - 1) for w in input().split())

bits = [0] * n
flips = 0
if c % 2 == 1:
    bits[0] = 1

for i in range(1, n):
    if i in broken:
        if bits[i - 1] == 1:
            flips += 1
    else:
        bits[i] = (bits[i - 1] + 1) % 2
        flips += 1
    if flips == c:
        break
print(''.join(str(b) for b in bits))

