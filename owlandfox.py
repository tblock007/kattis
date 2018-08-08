t = int(input())
for _ in range(t):
    n = [int(ch) for ch in list(input())]
    for i in range(len(n) - 1, -1, -1):
        if n[i] > 0:
            n[i:i+1] = [n[i] - 1]
            break
    print(int(''.join(str(ch) for ch in n)))
