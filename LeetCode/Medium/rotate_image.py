def transform(i, j, rows):
    # 0 -> 0, 0 -> 2
    # 0 -> 1, 1 -> 2
    # 0 -> 2, 2 -> 2

    # 1 -> 0, 0 -> 1
    # 1 -> 1, 1 -> 1
    # 1 -> 2, 2 -> 1

    # 2 -> 0, 0 -> 0
    # 2 -> 1, 1 -> 0
    # 2 -> 2, 2 -> 0

    # (3,2) 3 -> 2, 2 -> 0

    x = j
    y = rows - i - 1
    return x, y

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    seen = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            val_to_use = matrix[i][j]
            x, y = transform(i, j, rows)
            while (x,y) not in seen:
                seen.add((x,y))

                tmp = matrix[x][y]
                matrix[x][y] = val_to_use
                val_to_use = tmp
                x, y = transform(x, y, rows)


def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
printMatrix(matrix)
print()

rotate(matrix)
printMatrix(matrix)