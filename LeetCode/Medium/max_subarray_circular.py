def maxSubarraySumCircular(A):
    curr_best = 0
    curr_worst = 0
    total = 0
    best = float('-inf')
    worst = float('inf')
    largest_single = float('-inf')
    for num in A:
        total += num
        largest_single = max(largest_single, num)
        
        curr_best = max(curr_best + num, num)
        best = max(best, curr_best)
        
        curr_worst = min(curr_worst + num, num)
        worst = min(worst, curr_worst)
    
    # if all negative numbers, return largest of them
    if largest_single < 0:
        return largest_single
    
    # return the best connected sum or the total with worst sum stripped out
    return max(best, total - worst)

'''
Input
[-2,4,-5,4,-5,9,4]

Expected
15
'''
print(maxSubarraySumCircular([-2,4,-5,4,-5,9,4]))