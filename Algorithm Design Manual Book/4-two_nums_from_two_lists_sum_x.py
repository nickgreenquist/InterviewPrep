'''
4-6. Given two sets S1 and S2 (each of size n), and a number x, 
describe an O(nlogn) algorithm for finding whether there exists a pair of elements, 
one from S1 and one from S2, that add up to x. 
'''

def binary_search(nums, val):
    low = 0
    high = len(nums) - 1
    while low <= high:
        m = low + ((high - low) // 2)
        if nums[m] == val:
            return m
        if val < nums[m]:
            high = m - 1
        else:
            low = m + 1
    return -1


def findPairSum(nums1, nums2, x):
    # Sort nums1
    nums1 = sorted(nums1)

    # For each num in nums2, subtract x from it
    for num in nums2:
        r = x - num
        # binary search for remainder in sorted nums1
        index = binary_search(nums1, r)
        if index >= 0:
            return (nums1[index], num)
    return -1, -1


x = 4
nums1 = [3, 2, 7, 1]
nums2 = [3, 5, 6]

one, two = findPairSum(nums1, nums2, x)
print(one, two)