n = int(input())
l1, l2 = input(), input()
if n % 2 == 0:
    if l1 == l2:
        success = True
    else:
        success = False
elif n % 2 == 1:
    cl1 = ['1' if l1[i] == '0' else '0' for i in range(len(l1))]
    if ''.join(cl1) == l2:
        success = True
    else:
        success = False
print('Deletion succeeded' if success else 'Deletion failed')
    