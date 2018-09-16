
def traverse(board, i, j, k, word, seen):
    # we made it
    if k == len(word):
        return True
    
    key = str(i) + ',' + str(j)
    if key in seen:
        return False
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
    
    found = False
    if board[i][j] == word[k]:
        seen.add(key)
        found = found or traverse(board, i - 1, j, k + 1, word, seen)
        found = found or traverse(board, i + 1, j, k + 1, word, seen)
        found = found or traverse(board, i, j - 1, k + 1, word, seen)
        found = found or traverse(board, i, j + 1, k + 1, word, seen)
    
        if not found:
            seen.remove(key)
    return found

def exist(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            seen = set()
            found = traverse(board, i, j, 0, word, seen)
            if found:
                return True
    return False
                    

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]     
'''
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
print(exist(board, 'ABCCED'))
print(exist(board, 'SEE'))
print(exist(board, 'ABCB'))