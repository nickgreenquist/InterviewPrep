class Solution:
    def canPartition(self, nums):
        amount = 0
        for i in range(len(nums)):
            amount += nums[i]
            
        if amount % 2 != 0:
            return False
        
        amount = amount // 2
        
        dp = []
        for i in range(len(nums) + 1):
            dp.append([])
            for j in range(amount + 1):
                dp[i].append(False)
        
        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            dp[i][0] = True
        for j in range(1, amount + 1):
            dp[0][j] = False
        
        # offset by 1, so always considering nums[i-1] in our choice
        for i in range(1, len(nums) + 1):
            for j in range(1, amount + 1):
                # default choice is to skip nums[i-1]
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]: # we can use nums[i-1]
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
                
                # early stopping
                if dp[i][amount]:
                    return True         
        
        return dp[len(nums)][amount]

'''
Input: nums = [1,5,11,5]
Output: true
'''
s = Solution()
print(s.canPartition([1,5,11,5]))