words = input().split()
count = sum(1 if word.find('ae') != -1 else 0 for word in words)
if 5 * count / len(words) >= 2:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')