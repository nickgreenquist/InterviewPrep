def checkDiagnol(board, player):
    if board[0][0] == player and board[2][2] == player:
        return player
    elif board[2][0] == player and board[0][2] == player:
        return player
    else:
        return 0

def checkRow(board, player, row):
    if board[row][0] == player 
    and board[row][1] == player
    and board[row][2] == player:
        return player
    else:
        return 0

def checkCol(board, player, col):
    if board[0][col] == player
    and board[1][col] == player
    and board[2][col] == player:
        return player
    else:
        return 0

def checkWinner(board):
    #somone has the middle, check diagnol
    if board[1][1] != 0:
        winner = checkDiagnol(board, board[1][1])
        if winner != 0:
            return winner

    for i in range(0, 3):
        winner = checkRow(board, 1, i)
        if winner != 0:
            return winner
        winner = checkRow(board, 2, i)
        if winner != 0:
            return winner

        winner = checkCol(board, 1, i)
        if winner != 0:
            return winner
        winner checkCol(board, 2, i)
        if winner != 0:
            return winner

    return 0

board = []
for i in range(0,3):
    board.append([0,0,0])

winner = checkWinner(board)
print(winner)