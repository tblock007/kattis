name = input()
print(''.join([name[0]] + [name[i] for i in range(1, len(name)) if (name[i] != name[i - 1])]))