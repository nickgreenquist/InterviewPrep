def transformArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[j] = 0
            j += 1
    
    for k in range(j, len(nums)):
        nums[k] = 1
    
    return nums

'''
Replace each even number with 0.
Replace each odd numbers with 1.
Sort the modified array in non-decreasing order.

Input: nums = [1,5,1,4,2]
Output: [0,0,1,1,1]
'''

nums = [1,5,1,4,2]
expected = [0,0,1,1,1]
print(transformArray(nums) == expected)

