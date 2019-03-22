n = int(input())
print(sum((1 if input().find('CD') == -1 else 0) for i in range(n)))