
'''
Write an efficient algorithm that searches for a value in an m x n matrix. 

This matrix has the following properties:
 - Integers in each row are sorted in ascending from left to right.
 - Integers in each column are sorted in ascending from top to bottom.
'''
def binarySearch(nums, target):
    if len(nums) < 1:
        return False
    middle = len(nums) // 2
    if nums[middle] == target:
        return True
    if target > nums[middle]:
        return binarySearch(nums[middle + 1:],target)
    return binarySearch(nums[:middle],target)

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    for row in matrix:
        if binarySearch(row, target):
            return True
    return False

M = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(searchMatrix(M, 5))
print(searchMatrix(M, 20))
