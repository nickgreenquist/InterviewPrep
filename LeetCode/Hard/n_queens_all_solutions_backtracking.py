class Solution:
    def printState(self, state):
        for row in state:
            print(row)
        print()
    
    def isValidDiag(self, state, n, i, j):
        # check left-up diagnol
        x = i
        y = j
        while x >= 0 and y >= 0:
            if state[x][y] == 'Q':
                return False
            x -= 1
            y -= 1
        
        # check right-up diagnol
        x = i
        y = j
        while x >= 0 and y < n:
            if state[x][y] == 'Q':
                return False
            x -= 1
            y += 1
        
        return True
        
    
    def deepCopyState(self, state, n):
        copiedState = []
        for i in range(n):
            copiedState.append([])
            for j in range(n):
                copiedState[i].append(0)
        
        for i in range(n):
            for j in range(n):
                copiedState[i][j] = state[i][j]
                
        return copiedState
    
    def dfs(self, state, n, row, cols_used):
        if row == n:
            # self.printState(state)
            self.outputs.append(self.deepCopyState(state, n))
            return
        
        # at this row, place queen in every possible col and dfs to next row
        # pruning: if col already has queen in it, don't set
        # pruning: if row,col is hit by previous queen, don't set
        for col in range(n):
            if cols_used[col]:
                continue
            if not self.isValidDiag(state, n, row, col):
                continue
                
            state[row][col] = 'Q'
            cols_used[col] = 1
            
            self.dfs(state, n, row + 1, cols_used)
            
            # backtrack from this selection
            state[row][col] = '.'
            cols_used[col] = 0
        
    def solveNQueens(self, n):
        self.outputs = []
        
        state = []
        cols_used = []
        for i in range(n):
            state.append([])
            cols_used.append(0)
            for j in range(n):
                state[i].append('.')
        
        self.dfs(state, n, 0, cols_used)
        
        formattedOutputs = []
        for sol in self.outputs:
            singleOutput = []
            for row in sol:
                solRow = ""
                for char in row:
                    solRow += char
                singleOutput.append(solRow)
            formattedOutputs.append(singleOutput)
        return formattedOutputs
        
        
s = Solution()
solutions = s.solveNQueens(4)
for sol in solutions:
    for row in sol:
        print(row)
    print()