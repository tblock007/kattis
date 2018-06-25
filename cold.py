import sys

n = int(sys.stdin.readline())
print(len([t for t in sys.stdin.readline().split() if int(t) < 0]))