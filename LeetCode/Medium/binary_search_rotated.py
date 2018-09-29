def bsearch(nums, low, high, target):
    if low <= high:
        mid = low + ((high-low) // 2)
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target and target <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return bsearch(nums, low, high, target)
    return -1
            
def search(nums, target):
    return bsearch(nums, 0, len(nums), target)

'''
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''
print(search(nums = [4,5,6,7,0,1,2], target = 0))