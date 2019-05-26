import sys

for line in sys.stdin:
    print(sum(int(w) for w in line.split()) // 2)