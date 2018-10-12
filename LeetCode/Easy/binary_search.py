def binarySearch(nums, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binarySearch(nums, target, mid + 1, high)
        else:
            return binarySearch(nums, target, low, mid - 1)
        
    return -1

def search(nums, target):
    return binarySearch(nums, target, 0, len(nums) - 1)

'''
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
'''
print(search(nums = [-1,0,3,5,9,12], target = 9))

'''
Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
print(search(nums = [-1,0,3,5,9,12], target = 2))