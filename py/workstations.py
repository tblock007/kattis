import heapq

n, m = [int(w) for w in input().split()]
starts = []
ends = []
for _ in range(n):
    a, s = [int(w) for w in input().split()]
    starts.append(a)
    ends.append(a + s)
starts.sort()
ends.sort()

# heap representing available and unlocked workstations;
# value represents the time at which the station will lock
unlocked = []

next_start, next_end = 0, 0
count = 0
while next_start < len(starts):
    if ends[next_end] <= starts[next_start]:
        # a researcher is leaving - 
        # indicate that this workstation is potentially
        # reusable until a time m minutes from now
        heapq.heappush(unlocked, ends[next_end] + m)
        next_end += 1
    else:
        # a researcher is starting -
        # track all workstations that have locked in the meantime
        # by removing from unlocked
        while unlocked and unlocked[0] < starts[next_start]:
            heapq.heappop(unlocked)
        # if there are workstations left that are unlocked,
        # assign it to the researcher
        if unlocked:
            count += 1
            heapq.heappop(unlocked)
        next_start += 1
print(count)
