'''
Given a non-empty array, return true if there is a place to 
split the array so that the sum of the numbers on one side is equal 
to the sum of the numbers on the other side.
'''

def can_balance(arr):
    leftsum = 0
    rightsum = 0
    i = 0
    last_i = -1
    j = len(arr) - 1
    last_j = -1
    while i < j:
        if last_i != i:
            leftsum += arr[i]
            last_i = i
        if last_j != j:
            rightsum += arr[j]
            last_j = j
        if leftsum == rightsum:
            i += 1
            j -= 1
        else:
            if leftsum > rightsum:
                j -= 1
            else:
                i += 1
    if i == j: # midpoint
        if leftsum > rightsum:
            rightsum += arr[i]
        else:
            leftsum += arr[i]
    return leftsum == rightsum

print(can_balance([1, 1, 1, 2, 1])) # true
print(can_balance([2, 1, 1, 2, 1])) # false
print(can_balance([10, 10])) # true
print(can_balance([10,1,1,1,1,1,1,1,1,1,1])) # true