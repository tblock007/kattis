correct = [1, 1, 2, 2, 2, 8]
possess = [str(n - int(s)) for n, s in zip(correct, input().split())]
print(' '.join(possess))