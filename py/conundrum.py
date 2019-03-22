line = input()
print(len(line) - line[0::3].count('P') - line[1::3].count('E') - line[2::3].count('R'))