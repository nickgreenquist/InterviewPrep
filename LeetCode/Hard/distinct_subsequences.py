class Solution_Slow:
    def numDistinct(self, s: str, t: str) -> int:
        dp = []
        for i in range(len(s)):
            dp.append([])
            for j in range(len(t)):
                dp[i].append(0)
                
        hits = {}
        for i in range(len(t)):
            hits[i] = set()
            
        # first, let's mark last letter of t
        for i in range(len(s)):
            if s[i] == t[-1]:
                dp[i][len(t)-1] = 1
                hits[len(t)-1].add(i)
                
        # now, start moving back from t
        for j in range(len(t)-2, -1, -1):
            for i in range(0, len(s)):
                if s[i] == t[j]:
                    hits[j].add(i)
                    
                    # find how many hits for t[j+1] > i
                    for hit in hits[j+1]:
                        if hit > i:
                            dp[i][j] += dp[hit][j+1]
                
        for row in dp:
            print(row)
        print(hits)
        
        paths = 0
        for i in range(len(s)):
            paths += dp[i][0]
        return paths

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = []
        for i in range(len(s)+1):
            dp.append([])
            for j in range(len(t)+1):
                dp[i].append(0)
                
        # fill up last row matches to be equal to value 1 (made it)
        # if match, equal to 1 + value below in dp
        for i in range(len(s)-1, -1, -1):
            if t[len(t)-1] == s[i]:
                dp[i][len(t)-1] = dp[i+1][len(t)-1] + 1
            else:
                dp[i][len(t)-1] = dp[i+1][len(t)-1]
                
        for j in range(len(t)-2, -1, -1):
            for i in range(len(s)-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
            
        best = 0
        for i in range(len(s)):
            best = max(best, dp[i][0])
        return best

'''
Input: s = "babgbag", t = "bag"
Output: 5
'''

s = Solution()
print(s.numDistinct(s = "babgbag", t = "bag"))
