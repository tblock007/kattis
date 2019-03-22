# Performs the actual throw.  Updates variable curr 
# with the new result of throwing it a distance j
# The use of global here makes coding faster - we can 
# access curr and n variables without directly passing them to 
# the function (e.g., throw(j, n, curr)), but this should 
# only be used in a contest environment (i.e., NOT in 
# production code!).
# Separating this out into a function is not really necessary 
# since it is a pretty simple function, but it does help 
# reason about the main loop if we can trust that we have a 
# function that will simply handle the throw for us.
def throw(j):
    global n, curr
    curr += j
    curr %= n

# Read the input
n, k = [int(w) for w in input().split()]
tokens = [s for s in input().split()]

# A list that will be used as a stack (last-in-first-out) structure
# Every time a throw is made, it will be recorded (pushed onto) the stack.
# Every time an undo is needed, we will look at the top of the stack to 
# see how to undo it (and pop the value off the stack in the process).
stack = []

# Tracks current position; starts at child 0
curr = 0

# i will track the string we are on
i = 0
while i < len(tokens):
    # in the case of undo, we need to pop the appropriate amount off 
    # the stack, and undo each throw that we pop off
    if tokens[i] == 'undo':
        i += 1
        m = int(tokens[i])
        for _ in range(m):
            diff = stack.pop() # gets the most recent throw
            throw(-1 * diff) # "undoes" it by throwing in the opposite direction
    # in the simple case of a number, we need only execute the throw
    else:
        diff = int(tokens[i])
        throw(diff)
        stack.append(diff) # make sure that every throw that gets made is recorded on the stack
    i += 1

# The process is complete, so we can simply print out the result.
print(curr)