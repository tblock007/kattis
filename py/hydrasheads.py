while True:
	h, t = [int(w) for w in input().split()]
	if h == 0 and t == 0:
		break
	
	count = 0

	if h % 2 == 1 and t == 0:
		print(-1)
	else:
		# first step - get an appropriate number of tails
		# note: we could also compute the number of tails we need to add as follows:
		# if h % 2 == 1:
        #     addtails = (2 - (t % 4)) % 4
        # else:
        #     addtails = (0 - (t % 4)) % 4
		if h % 2 == 1:
			while t % 4 != 2:
				t += 1
				count += 1
		else:
			while t % 4 != 0:
				t += 1
				count += 1
		
		# second step - convert tails to heads
		h += (t // 2)
		count += (t // 2)

		# third step - cut off all heads
		count += (h // 2)

		print(count)

