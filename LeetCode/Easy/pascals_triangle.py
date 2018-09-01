'''
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
def pascals_triangle(numRows):
        triangle = []
        for i in range(numRows):
            size = i + 1
            row = [0]*size
            row[0] = 1
            row[-1] = 1
            if i > 0:
                for j in range(1, size - 1):
                    row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle

triangle = pascals_triangle(5)
for row in triangle:
    print(row)