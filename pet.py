import sys

scores = [sum([int(num) for num in line.split()]) for line in sys.stdin.readlines()]
print('{0} {1}'.format(scores.index(max(scores)) + 1, max(scores)))