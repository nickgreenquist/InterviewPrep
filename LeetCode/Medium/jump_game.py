'''
You are given an integer array nums.
You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return TRUE if you can reach the last index, or FALSE otherwise.
'''

def jump(nums, i, lookup):
    if i == len(nums) - 1:
        return True
    if i >= len(nums):
        return False
    
    if i in lookup:
        return lookup[i]
    
    for j in range(nums[i], 0, -1):
        dest = i + j
        if dest in lookup:
            return lookup[dest]
        
        can_reach = jump(nums, dest, lookup)
        if can_reach:
            lookup[i] = True
            return True
    
    lookup[i] = False
    return False

def jumpLoop(nums, lookup):
    for i in range(len(nums) - 2, -1, -1):
        for j in range(nums[i], -1, -1):
            if i + j >= len(nums):
                lookup[i] = False
            if i + j == len(nums) - 1:
                lookup[i] = True
                break
            if i+j in lookup and lookup[i+j]:
                lookup[i] = True
                break
            lookup[i+j] = False
    return lookup[0]

def jumpGreedy(nums):
    gas = 0
    for n in nums:
        print(gas, n)
        if gas < 0:
            return False
        elif n > gas:
            print('taking: ', n)
            gas = n
        gas -= 1

    return True
    

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    lookup = {}
    # can_reach = jump(nums, 0, lookup)
    # can_reach = jumpLoop(nums, lookup)
    can_reach = jumpGreedy(nums)
    return can_reach 



'''
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

nums = [2,3,1,1,4]
print(canJump(nums))