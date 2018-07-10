from sys import stdin
w = int(stdin.readline())
n = int(stdin.readline())
area = 0
for line in stdin.readlines():
    a, b = [int(c) for c in line.split()]
    area = area + (a * b)
print(round(area / w))
