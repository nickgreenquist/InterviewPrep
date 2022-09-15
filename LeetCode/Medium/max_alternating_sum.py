class Solution:   
    def maxAlternatingSum(self, nums):
        dp = {}
        for i in range(-1, len(nums)):
            dp[(i, 1)] = 0
            dp[(i, -1)] = 0
        
        for i in range(len(nums)):
            dp[(i, 1)] = max(dp[(i-1, -1)] + nums[i], dp[(i-1, 1)])
            dp[(i, -1)] = max(dp[(i-1, 1)] - nums[i], dp[(i-1, -1)])
        
        best = 0
        for k,v in dp.items():
            best = max(best, v)
        return best

'''
Input: nums = [6,2,1,2,4,5]
Output: 10
'''
s = Solution()
print(s.maxAlternatingSum([6,2,1,2,4,5]))
