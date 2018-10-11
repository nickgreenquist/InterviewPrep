'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
'''

def merge(nums1, m, nums2, n):
    if n < 1:
        return
    
    i = 0
    j = 0
    while i < m:
        if nums1[i] < nums2[j]:
            i += 1
        else:
            nums1[i], nums2[j] = nums2[j], nums1[i]
            i += 1
            
            # put the swapped in number into the right slot
            if n > 1:
                k = j
                while k < n - 1 and nums2[k] > nums2[k+1]:
                    nums2[k], nums2[k+1] = nums2[k+1], nums2[k]
                    k += 1
    
    # everything left in nums2 just gets appended to the 0 slots
    for j in range(n):
        nums1[i] = nums2[j]
        i += 1

'''
Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)