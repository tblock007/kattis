n = int(input())
for i in range(n):
    name, study_start, dob, c = input().split()
    print(name, end=' ')
    sy, sm, sd = [int(w) for w in study_start.split('/')]
    dy, dm, dd = [int(w) for w in dob.split('/')]
    courses = int(c)
    if sy >= 2010:
        print('eligible')
    elif dy >= 1991:
        print('eligible')
    elif courses >= 41:
        print('ineligible')
    else:
        print('coach petitions')