# prints a 2D list of characters
def printGrid(grid):
	for i in range(len(grid)):
		print(''.join(grid[i]))



		

# finds the starting position in the fun house by 
# checking for the '*' character, as well as the initial 
# direction
# note that the initial direction of the trace is also 
# completely determined by which wall contains the starting
# point
def findStart(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == '*':
				if i == 0:
					d = 'S'
				elif i == len(grid) - 1:
					d = 'N'
				elif j == 0:
					d = 'E'
				elif j == len(grid[i]) - 1:
					d = 'W'
				return i, j, d





# performs the actual trace through the funhouse by
# stepping one grid point at a time
def trace(grid, i, j, d):
	# we know that our trace must end at a wall ('x' character), 
	# and we can stop once we hit a wall
	while grid[i][j] != 'x':

		# if we've reached a mirror, we want to update the direction 
		# first before stepping forward
		if grid[i][j] == '/':
			if d == 'N':
				d = 'E'
			elif d == 'S':
				d = 'W'
			elif d == 'E':
				d = 'N'
			elif d == 'W':
				d = 'S'
		elif grid[i][j] == '\\':
			if d == 'N':
				d = 'W'
			elif d == 'S':
				d = 'E'
			elif d == 'E':
				d = 'S'
			elif d == 'W':
				d = 'N'

		# at this point, we've taken care of the direction, 
		# so we can simply update the position
		if d == 'N':
			i = i - 1
		elif d == 'S':
			i = i + 1
		elif d == 'E':
			j = j + 1
		elif d == 'W':
			j = j - 1

	# when the while loop exits, we have reached the wall, so we can return the position we found
	return i, j





# the actual solution - uses the functions defined above to 
# find the starting point, trace to the end, and place the exit
def solve(grid):
	i, j, d = findStart(grid)
	fi, fj = trace(grid, i, j, d)
	grid[fi][fj] = '&'
	printGrid(grid)




house = 1
while True:
	w, l = [int(w) for w in input().split()]
	if w == 0 and l == 0:
		break
	
	grid = [[c for c in input()] for i in range(l)]
	print('HOUSE {0}'.format(house))
	house += 1
	solve(grid)
	