n, m = [int(w) for w in input().split()]
blanks = set(i for i in range(m))
for _ in range(n):
    s = input()
    b = set(i for i in range(m) if s[i] == '_')
    blanks = blanks & b
print(len(blanks) + 1)