'''
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
'''

def binarySearch(nums, low, high, target):
    if low <= high:
        mid = (high+low)//2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            return binarySearch(nums, low, mid-1, target)
        else:
            return binarySearch(nums, mid+1, high, target)
    return -1

def searchRange(nums, target):
    hit = binarySearch(nums, 0, len(nums) - 1, target)
    if hit == -1:
        return [hit, hit]
    
    # find the first occurence
    low = hit
    while low >= 0 and nums[low] == target:
        low -= 1
    
    # find the last occurence
    high = hit
    while high < len(nums) and nums[high] == target:
        high += 1
    
    return [low + 1, high - 1]

'''
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''
print(searchRange(nums = [5,7,7,8,8,10], target = 8))

'''
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
print(searchRange(nums = [5,7,7,8,8,10], target = 6))