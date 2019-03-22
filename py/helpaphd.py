import sys
sys.stdin.readline()
for line in sys.stdin.readlines():
	print('skipped' if (line.find('P=NP') != -1) else eval(line))