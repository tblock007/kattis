import bisect

def possible(i, j):
    if (i == '1'): return True
    if (i == '2'): return (j in ['2', '3', '5', '6', '8', '9', '0'])
    if (i == '3'): return (j in ['3', '6', '9'])
    if (i == '4'): return (j in ['4', '5', '6', '7', '8', '9', '0'])
    if (i == '5'): return (j in ['5', '6', '8', '9', '0'])
    if (i == '6'): return (j in ['6', '9'])
    if (i == '7'): return (j in ['7', '8', '9', '0'])
    if (i == '8'): return (j in ['8', '9', '0'])
    if (i == '9'): return (j == '9')
    if (i == '0'): return (j == '0')
    

def check(num):
    for i in range(len(num) - 1):
        if (not possible(num[i], num[i + 1])):
            return False
    return True    


valid = [i for i in range(1, 201) if check(str(i))]
n = int(input())
for i in range(n):
    k = int(input())
    if k == 200:
        print(200)
    else:
        gi = bisect.bisect_right(valid, k)
        cand1 = valid[gi - 1]
        cand2 = valid[gi]
        print(cand1 if ((cand2 - k) > (k - cand1)) else cand2)
