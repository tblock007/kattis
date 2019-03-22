import sys
d = [int(w) for w in sys.stdin.readlines()]
s = sum(d) - 100
for i in range(len(d)):
    for j in range(i + 1, len(d)):
        if (d[i] + d[j] == s):
            rd = [d[ii] for ii in range(len(d)) if ii != i and ii != j]
            for r in rd:
                print(r)
            sys.exit()