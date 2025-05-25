def buildArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return [nums[nums[i]] for i in range(len(nums))]

nums = [0,2,1,5,3,4]
expected = [0,1,2,4,5,3]
print(buildArray(nums) == expected)