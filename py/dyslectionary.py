# reverses a string; defining this as a function that takes a 
# string as an argument allows us to sort by reversed string
def reverseString(s):
	return s[::-1]

# sort appropriately, and then output the list with the specified
# formatting
def solve(words, mlen):
	words.sort(key = reverseString)
	for w in words:
		print('{0}{1}'.format(' ' * (mlen - len(w)), w))

# the use of try-except here allows us to read until the end of input
while True:
	try:
		words = []
		mlen = -1
		while True:
			w = input()
			if w == "":
				break
			words.append(w)
			if len(w) > mlen:
				mlen = len(w)

		solve(words, mlen)
		print()		

	except EOFError:
		# since we break out as soon as we finish reading the input, 
		# we still need to solve the final case
		solve(words, mlen) 
		break

