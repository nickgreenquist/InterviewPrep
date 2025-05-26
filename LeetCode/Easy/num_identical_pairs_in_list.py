def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = {}

    for num in nums:
        if num not in count:
            count[num] = 0
        count[num] += 1
    
    output = 0
    for num in nums:
        count[num] -= 1
        output += count[num]
    
    return output

'''
Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
'''

nums = [1,2,3,1,1,3]
print(nums, "->", numIdenticalPairs(nums))

nums = [1,1,1,1]
print(nums, "->", numIdenticalPairs(nums))