n, m = [int(w) for w in input().split()]
if n > m:
    print('Dr. Chaz needs {0} more piece{1} of chicken!'.format(n - m, '' if (n - m == 1) else 's'))
elif m > n:
    print('Dr. Chaz will have {0} piece{1} of chicken left over!'.format(m - n, '' if (m - n == 1) else 's'))