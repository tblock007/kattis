line = input()
indices = range(len(line))
i_iter = iter(indices)
result = []
for i in i_iter:
    result.append(line[i])
    if ((i < len(indices) - 2) and (line[i] in ['a', 'e', 'i', 'o', 'u'] and line[i] == line[i + 2] and line[i + 1] == 'p')):        
        next(i_iter)
        next(i_iter)
print(''.join(result))