b, k, g = [int(w) for w in input().split()]

b -= 1 # account for the fact that the troll is not under the original bridge
ng = k // g # determine the number of groups that can be formed

# now two cases can occur: either there are a number of groups that evenly 
# divides the number of bridges to be checked, or there are leftover bridges that 
# require an additional run
print((b // ng) if b % ng == 0 else (b // ng + 1))