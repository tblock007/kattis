import heapq
from collections import deque

# we use this while True in combination with try and except EOFError in
# order to read to the end of the input
while True:
	try:
		n = int(input())

		# we will simply simulate the process with each data structure 
		# and track violations
		s, q, pq = deque(), deque(), []

		# dictates whether this structure can be a stack, queue, or priority queue
		isStack, isQueue, isPQueue = True, True, True 
		
		for _ in range(n):
			c, v = [int(w) for w in input().split()]
			if c == 1:
				s.append(v)
				q.append(v)
				heapq.heappush(pq, -1 * v)			
			else:
				if len(s) == 0 or v != s.pop():
					isStack = False
				if len(q) == 0 or v != q.popleft():
					isQueue = False
				if len(pq) == 0 or v != -1 * heapq.heappop(pq):
					isPQueue = False
		
		poss = (1 if isStack else 0) + (1 if isQueue else 0) + (1 if isPQueue else 0)
		if poss == 0:
			print('impossible')
		elif poss > 1:
			print('not sure')
		elif isStack:
			print('stack')
		elif isQueue:
			print('queue')
		elif isPQueue:
			print('priority queue')	

	except EOFError:
		break
