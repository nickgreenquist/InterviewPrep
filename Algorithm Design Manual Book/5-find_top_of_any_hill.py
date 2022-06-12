def bs(arr, L, H):
    range_size = H - L
    if range_size <= 1 and L == 0:
        return 0
    if range_size <= 1:
        return None
    
    m = L + ((range_size) // 2)
    
    peak_versus_left =  m-1 < 0 or (arr[m] > arr[m-1])
    peak_versus_right = m+1 >= len(arr) or (arr[m] > arr[m+1])
    if peak_versus_left and peak_versus_right:
        return m
    
    # go in direction of rising slope
    if m+1 < H and arr[m] < arr[m+1]:
        return bs(arr, m, H)
    else:
        return bs(arr, L, m)
    
def findPeakElement(nums):
    return bs(nums, 0, len(nums))

'''
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
'''
nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))
        