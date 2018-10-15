'''
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative. 
A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative.
In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence.
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence,
leaving the remaining elements in their original order.
'''
def wiggleMaxLength(nums):
    if len(nums) < 2:
        return len(nums)
    if len(set(nums)) == 1:
        return 1
    
    # make a list of all the differences between pairs of numbers
    wiggle = []
    for i in range(len(nums) - 1):
        wiggle.append(nums[i+1] - nums[i])
    
    best = float('-inf')
    count = 1
    i = 0
    j = 1
    while j < len(wiggle):
        # we can't use zero differences to simply iterate past them
        while wiggle[j] == 0:
            j += 1
        while wiggle[i] == 0:
            i += 1
            
        # there is a wiggle if the product of the diff between two pairs is negative
        if wiggle[j] * wiggle[i] < 0:
            count += 1
            best = max(best, count)
            i = j
            j += 1
            
        # if no wiggle, move the lookahead pointer up one
        else:
            j += 1
    best = max(best, count)
    return best + 1

'''
Example 1:
Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
'''
print(wiggleMaxLength([1,7,4,9,2,5]))

'''
Example 2:
Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
'''
print(wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))

'''
Example 3:
Input: [1,2,3,4,5,6,7,8,9]
Output: 2
'''
print(wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
