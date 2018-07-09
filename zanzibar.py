n = int(input())
for i in range(n):
    seq = [int(w) for w in input().split()[:-1]]
    lb = sum((seq[j] - (2 * seq[j - 1])) for j in range(1, len(seq)) if (seq[j] > 2 * seq[j - 1]))
    print(lb)