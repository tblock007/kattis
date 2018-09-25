def isarith(seq):
    diff = seq[1] - seq[0]
    for i in range(2, len(seq)):
        if seq[i] - seq[i-1] != diff:
            return False
    return True


n = int(input())
for i in range(n):
    seq = [int(w) for w in input().split()][1:]
    if isarith(seq):
        print('arithmetic')
    elif isarith(sorted(seq)):
        print('permuted arithmetic')
    else:
        print('non-arithmetic')