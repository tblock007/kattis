n = int(input())
for i in range(n):
    l1, l2 = input(), input()
    print(l1)
    print(l2)
    for j in range(len(l1)):
        print('.' if l1[j] == l2[j] else '*', end='')
    print()