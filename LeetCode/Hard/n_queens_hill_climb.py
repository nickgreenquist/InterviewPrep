import random

class Solution:
    def printState(self, state):
        for row in state:
            print(row)
        print()
            
    def checkRows(self, state, n, i, j):
        score = 0
        for row in range(n):
            if row != i and state[row][j] == 1:
                score += 1
        return score
    
    def checkCols(self, state, n, i, j):
        score = 0
        for col in range(n):
            if col != j and state[i][col] == 1:
                score += 1
        return score
    
    def checkDiag(self, state, n, i, j):
        x = i
        y = j
        score = 0
        
        while x > 0 and y > 0:
            if state[x][y] == 1 and not (x == i and y == j):
                score += 1
            x -= 1
            y -= 1
        x = i
        y = j
            
        while x > 0 and y < n:
            if state[x][y] == 1 and not (x == i and y == j):
                score += 1
            x -= 1
            y += 1
        x = i
        y = j
            
        while x < n and y > 0:
            if state[x][y] == 1 and not (x == i and y == j):
                score += 1
            x += 1
            y -= 1
        x = i
        y = j
            
        while x < n and y < n:
            if state[x][y] == 1 and not (x == i and y == j):
                score += 1
            x += 1
            y += 1
            
        return score
        
    def score(self, state, n):
        score = 0
        for i in range(n):
            for j in range(n):
                if state[i][j] == 1:
                    score += self.checkRows(state, n, i, j) + self.checkCols(state, n, i, j) + self.checkDiag(state, n, i, j)
        
        return score
    
    def makeMove(self, state, n, queens, current_score):
        
        moves = {}
        for i in range(n):
            cur_col = queens[i]
            for j in range(n):
                state[i][j] = 1
                state[i][cur_col] = 0
                moves[(i,j)] = self.score(state, n)
                state[i][j] = 0
                state[i][cur_col] = 1
        
        score_to_beat = current_score
        for k,v in moves.items():
            if v < score_to_beat:
                score_to_beat = v
        
        best_moves = []
        for k,v in moves.items():
            if v == score_to_beat:
                best_moves.append(k)
                
        # pick a random best move
        if len(best_moves) > 0:
            pick = random.randint(0,len(best_moves) - 1)
            row = best_moves[pick][0]
            col = best_moves[pick][1]
            
            cur_col = queens[i]
            state[row][cur_col] = 0
            state[row][col] = 1
            queens[row] = col
        
        return score_to_beat
    
    def hillClimb(self, n):
        self.done = False
        
        state = []
        for i in range(n):
            state.append([])
            for j in range(n):
                state[i].append(0)
        
        # randomly place N queens
        queens = {}
        for row in range(n):
            col = random.randint(0, n-1)
            state[row][col] = 1
            queens[row] = col
        
        for i in range(n*n*2):
            current_score = self.score(state, n)
            if current_score == 0:
                return state, queens
            
            new_score = self.makeMove(state, n, queens, current_score)
            if current_score == new_score:
                break
        
        return None, None
        
    def solveNQueens(self, n):
        self.done = False
        
        for i in range(n*10):
            state, queens = self.hillClimb(n)
            if state:
                return state

        return None
        
s = Solution()
state = s.solveNQueens(5)
for row in state:
    print(row)
            
        
        
        