c = float(input())
l = int(input())

sum = 0
for i in range(l):
    w, h = map(float, input().split())
    sum += c * w * h
print(sum, end='')