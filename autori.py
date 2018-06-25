s = input()
for char in (filter(lambda c: c.isupper(), s)):
    print(char, end='')
print()
