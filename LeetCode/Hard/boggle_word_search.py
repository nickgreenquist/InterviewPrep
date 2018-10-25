'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.
'''
def dfs(board, i, j, seen, words, prefix, trie, out):
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
        return
    if (i,j) in seen:
        return
    
    prefix += board[i][j]
    if board[i][j] in trie and '#' in trie[board[i][j]]:
        out.add(prefix)
    
    for tup in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
        x = tup[0]
        y = tup[1]
        if board[i][j] in trie:
            seen.add((i,j))
            dfs(board, x, y, seen, words, prefix, trie[board[i][j]], out)
            seen.remove((i,j))
    
def findWords(board, words):
    # set up a Trie - dictionary of dictionaries
    trie={}
    for w in words:
        t=trie
        for c in w:
            if c not in t:
                t[c]={}
            t=t[c]
        t['#']='#' # signal a complete word
        
    out = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            seen = set()
            dfs(board, i, j, seen, words, "", trie, out)
    return list(out)

''' Example: '''
print(findWords(words = ["oath","pea","eat","rain"], board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]))
''' Output: ["eat","oath"] '''