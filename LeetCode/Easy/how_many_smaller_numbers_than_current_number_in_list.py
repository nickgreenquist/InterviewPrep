def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sorted_nums = sorted(nums)

    nums_to_i = {}
    for i in range(len(sorted_nums)):
        num = sorted_nums[i]
        if num not in nums_to_i:
            nums_to_i[num] = i
    
    for i in range(len(nums)):
        num = nums[i]
        idx_in_sorted = nums_to_i[num]

        nums[i] = idx_in_sorted
    return nums

'''
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
'''
nums = [8,1,2,2,3]
expected = [4,0,1,1,3]
print(smallerNumbersThanCurrent(nums) == expected)