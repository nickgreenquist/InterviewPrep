def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def checkBoard(board, row, row_seen, col_seen, grid_seen):
    for col in range(9):
        num = board[row][col]
        if not is_number(num):
            continue
        
        # check for valid row and col and grid
        if num in row_seen[row] or num in col_seen[col] or num in grid_seen[row//3][col//3]:
            return False
        row_seen[row].add(num)
        col_seen[col].add(num)
        grid_seen[row//3][col//3].add(num)
        
    return True
    
    
def isValidSudoku(board):
    row_seen = [set() for i in range(9)]
    col_seen = [set() for i in range(9)]
    grid_seen = [[set() for j in range(3)] for i in range(3)]
    for i in range(9):
        if not checkBoard(board, i, row_seen, col_seen, grid_seen):
            return False
    return True

'''
Example 1:
Output: true
'''
print(isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

'''
Example 2:
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''
print(isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

# Solution 2
class Solution:
    def checkRows(self, board):
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            seen = set()
            for j in range(cols):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        return True
                
        
    def checkColumns(self, board):
        rows = len(board)
        cols = len(board[0])
        for i in range(cols):
            seen = set()
            for j in range(rows):
                if board[j][i] == '.':
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        return True
        
    def checkGrids(self, board):
        for i in range(3):
            for j in range(3):
                seen = set()
                for k in range(3):
                    for p in range(3):
                        row = (i * 3) + k
                        col = (j * 3) + p
                        val = board[row][col]
                        if val == '.':
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True
        
    def isValidSudoku(self, board):
        areRowsValid = self.checkRows(board)
        areColsValid = self.checkColumns(board)
        areGridsValid = self.checkGrids(board)
        
        return areRowsValid and areColsValid and areGridsValid