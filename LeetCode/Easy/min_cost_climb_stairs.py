class Solution:
    def climb(self, i, cost, dp):
        if i < 0:
            return 0
        if i == 0 or i == 1:
            return dp[i]
        
        if dp[i] != 0:
            return dp[i]
        
        dp[i] = cost[i] + min(self.climb(i-1, cost, dp), self.climb(i-2, cost, dp))
        return dp[i]
        
    def minCostClimbingStairs(self, cost) -> int:
        dp = [0 for i in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        return min(self.climb(len(cost)-1, cost, dp), self.climb(len(cost)-2, cost, dp))

'''
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
'''
s = Solution()

print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))