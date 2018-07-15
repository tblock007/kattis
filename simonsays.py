n = int(input())
for i in range(n):
    line = input()
    if line.find('Simon says') == 0:
        print(line[11:])