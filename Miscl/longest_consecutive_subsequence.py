
'''
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 1:
        return 0
    nums_set = set(nums)
    fronts = []
    for n in nums:
        if n + 1 in nums_set and n - 1 not in nums_set:
            fronts.append(n)
    
    max_length = 1
    for n in fronts:
        current_length = 0
        while n in nums_set:
            current_length += 1
            n += 1
        max_length = max(max_length, current_length)
    return max_length

print(longestConsecutive([100, 4, 200, 1, 3, 2]))
