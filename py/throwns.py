def throw(j):
    global n, curr
    curr += j
    curr %= n

n, k = [int(w) for w in input().split()]
tokens = [s for s in input().split()]
stack = []
curr = 0

i = 0
while i < len(tokens):
    if tokens[i] == 'undo':
        i += 1
        m = int(tokens[i])
        for _ in range(m):
            diff = stack.pop()
            throw(-1 * diff)
    else:
        diff = int(tokens[i])
        throw(diff)
        stack.append(diff)
    i += 1

print(curr)