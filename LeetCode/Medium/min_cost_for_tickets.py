class Solution:         
    def mincostTickets(self, days, costs):
        dp = []
        nums = []
        for i in range(0, max(days) + 1):
            nums.append(i)
            dp.append(0)
            
        days_set = set(days)
        
        dp[max(days)] = 0
        
        for i in range(len(nums)-1, 0, -1):
            if i not in days_set:
                if i < len(nums)-1:
                    dp[i] = dp[i+1]
                continue
                
            # one day ticket
            daily = costs[0]
            if i < len(nums) - 1:
                daily += dp[i+1]
            
            # week ticket
            weekly = costs[1]
            if i + 7 < len(nums):
                weekly += dp[i + 7]
            
            # monthly
            monthly = costs[2]
            if i + 30 < len(nums):
                monthly += dp[i + 30]
            
            dp[i] = min(daily, weekly, monthly)
        
        return dp[min(days)]

'''
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
'''

s = Solution()
print(s.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))