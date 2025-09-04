def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    res = 0
    left = 0
    right = 0
    while right < len(nums) - 1:
        max_reach = 0
        for i in range(left, right + 1):
            max_reach = max(max_reach, i + nums[i])

        left = right + 1
        right = max(right, max_reach)
        res += 1
    return res

'''
Input: nums = [2,3,1,1,4]
Output: 2
'''
print(jump([2,3,1,1,4]))