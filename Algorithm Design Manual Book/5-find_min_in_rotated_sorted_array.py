def findk(nums, L, H):
    if L >= H:
        return 0
    
    m = L + ((H - L) // 2)
    
    if m+1 < H and nums[m] > nums[m+1]:
        return m + 1
    elif m >= 1 and nums[m] < nums[m-1]:
        return m
    
    # go left or right?
    if nums[m] < nums[0]:
        return findk(nums, L, m)
    else:
        return findk(nums, m + 1, H)
    
def findMin(nums):
    k = findk(nums, 0, len(nums))
    return nums[k]

'''
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
'''

nums = [4,5,6,7,0,1,2]
print(findMin(nums))