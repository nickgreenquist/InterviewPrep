from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.num_words = 0
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
            
        node.isWord = True
        self.num_words += 1
        
class Solution:
    def dfs(self, board, m, n, x, y, visited, trie, node, currentWord):   
        if not node or trie.num_words == 0:
            return
        if x < 0 or x >= m or y < 0 or y >= n:
            return
        
        if visited[x][y]:
            return
        
        if node.isWord:
            self.output.append(currentWord)
            node.isWord = False
            trie.num_words -= 1
        
        visited[x][y] = 1
        for i,j in [(x+1, y),(x-1, y),(x, y+1),(x, y-1)]:
            if not (i < 0 or i >= m or j < 0 or j >= n):
                c = board[i][j]
                self.dfs(board, m, n, i, j, visited, trie, node.children.get(c), currentWord + c)
        visited[x][y] = 0
    
    def findWords(self, board, words):
        m = len(board)
        n = len(board[0])
        
        visited = []
        for i in range(m):
            visited.append([])
            for j in range(n):
                visited[i].append(0)
        
        self.output = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
            
        for i in range(m):
            for j in range(n):
                self.dfs(board, m, n, i, j, visited, trie, node.children[board[i][j]], board[i][j])
                
        return self.output
        
''' Example: '''
s = Solution()
print(s.findWords(words = ["oath","pea","eat","rain"], board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]))
''' Output: ["eat","oath"] '''