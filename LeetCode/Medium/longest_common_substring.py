class Solution:  
    def longestCommonSubstring(self, x: str, y: str) -> int:
        dp = []
        for i in range(len(x) + 1):
            dp.append([])
            for j in range(len(y) + 1):
                dp[i].append(0)

        max_seen = 0
        for i in range(len(x) + 1):
            for j in range(len(y) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif x[i-1] == y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                max_seen = max(max_seen, dp[i][j])
        
        return max_seen
        

'''
Input : X = “zxabcdezy”, y = “yzabcdezx” 
Output : 6 
Explanation:
The longest common substring is “abcdez” and is of length 6.
'''
s = Solution()
print(s.longestCommonSubstring(x = "zxabcdezy", y = "yzabcdezx" ))
