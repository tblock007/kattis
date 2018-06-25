x = int(input())
n = int(input())

sum = 0
for i in range(n):
    p = int(input())
    sum += p

ans = (x * (n + 1)) - sum
print(ans, end='')
