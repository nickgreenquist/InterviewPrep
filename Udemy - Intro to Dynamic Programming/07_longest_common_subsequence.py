class Solution:
    
    def dfs(self, t1, t2, i, j, dp):
        if i >= len(t1):
            return 0
        if j >= len(t2):
            return 0
        if (i,j) in dp:
            return dp[(i,j)]
        
        best = 0
        if t1[i] == t2[j]:
            best = self.dfs(t1, t2, i + 1, j + 1, dp) + 1
        else:
            best = max(self.dfs(t1, t2, i + 1, j, dp), self.dfs(t1, t2, i, j + 1, dp))
        dp[(i,j)] = best
        return best
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        
        self.dfs(text1, text2, 0, 0, dp)
        
        best = 0
        for k,v in dp.items():
            best = max(best, v)
        return v

'''
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
'''
s = Solution()
print(s.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))