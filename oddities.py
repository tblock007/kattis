import sys
sys.stdin.readline()
for i in [int(n) for n in sys.stdin.readlines()]:
    print('{0} is {1}'.format(i, 'even' if (i % 2 == 0) else 'odd'))