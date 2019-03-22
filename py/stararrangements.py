s = int(input())
print(s, end=':\n')
for i in range(2, s):
    if (s % (2 * i - 1) == 0 or (s - i) % (2 * i - 1) == 0):
        print('{0},{1}'.format(i, i - 1))
    if (s % i == 0):
        print('{0},{1}'.format(i, i))