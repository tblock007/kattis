n = int(input())
sum = 0
for i in range(n):
    s = input()
    b, e = int(s[:-1]), int(s[-1])
    sum += b**e
print(sum)
