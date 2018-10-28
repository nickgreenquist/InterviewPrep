'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''
def spiralOrder(matrix):
    if not matrix:
        return []
    out = []
    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1
    
    while left <= right and top <= bottom:
        # get top row
        for i in range(left, right+1):
            out.append(matrix[top][i])
        
        # get right col
        for i in range(top+1, bottom+1):
            out.append(matrix[i][right])
        
        # get bottom row
        if bottom - top > 0:
            for i in range(right-1, left-1, -1):
                out.append(matrix[bottom][i])
        
        # get left col
        if right - left > 0:
            for i in range(bottom-1, top, -1):
                out.append(matrix[i][left])
        
        top += 1
        bottom -= 1
        
        left += 1
        right -= 1
    
    return out

'''
Example 1:
Output: [1,2,3,6,9,8,7,4,5]
'''
print(spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))

'''
Example 2:
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
print(spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))