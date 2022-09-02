class Solution:     
    def validMove(self, x, y, num):
        # check rows
        for i in range(9):
            if self.board[i][y] == num:
                return False
        
        # check cols
        for i in range(9):
            if self.board[x][i] == num:
                return False
        
        # check grids
        grid_x = (x // 3) * 3
        grid_y = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[grid_x + i][grid_y + j] == num:
                    return False
        
        return True
        
    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == ".":
                    for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        if self.validMove(i, j, num):
                            self.board[i][j] = num
                            if self.solve():
                                return True
                            else:
                                self.board[i][j] = '.' # backtrack
                            
                    return False # if we check every possible number, and none work for empty cell, we return early
        return True
        
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

s = Solution()
s.solveSudoku(board)
for row in board:
    print(row)