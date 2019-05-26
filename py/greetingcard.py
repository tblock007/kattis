# this turns out to be another problem that is quite easy to understand 
# and even solve for small input sizes, but the "easy" solution ends up being 
# too slow.  we could just check every pair of points and see if they are 2018 
# apart, but this will be too slow if they give us 100,000 points.

# a key insight to this problem is that each point can only occur at INTEGER 
# coordinates; that means that for every point, we only need to check TWELVE 
# surrounding points to see whether they're there: the four that are directly 
# north/east/south/west of the point, and eight more according to the 
# Pythagorean triple 1118-1680-2018 (this hint is given in Sample Input #2)

# a little bit of number theory is needed to convince ourselves that these 
# twelve points are the ONLY points we need to check.  since the prime 
# factorization of 2018 is 2 * 1009, it turns out there is only one triple that 
# has 2018 on the hypotenuse.

# a trick used here so that we can use a for loop to iterate over the twelve 
# points we need to check; if we are interested in checking points around (x, y), 
# we can iterate over the twelve surrounding candidate points by checking all of 
# (x + dx[i], y + dy[i])
dx = [0, 1118, 1680, 2018, 1680, 1118, 0, -1118, -1680, -2018, -1680, -1118]
dy = [2018, 1680, 1118, 0, -1118, -1680, -2018, -1680, -1118, 0, 1118, 1680]

n = int(input())

# read in each point and add it to a set
# we use a set data structure here because it allows us to very quickly 
# check for membership; i.e., quickly determine whether a point is in the set
points = set()
for _ in range(n):
	x, y = [int(w) for w in input().split()]
	points.add((x, y))

# keep a count of every time a point is found that is exactly 2018 from another point
count = 0
for p in points:
	for i in range(len(dx)):
		if (p[0] + dx[i], p[1] + dy[i]) in points:
			count += 1

# note that this will double count each segment, since we will count each pair twice
# rather than worry about preventing the double counting, we will just divide by 2 at the end
print(count // 2)