class Solution:
    def move(self, nums, n, i, memo):
        if i >= n:
            return 0
        if i in memo:
            return memo[i]
        
        rob_this_house = nums[i]
        rob_next_house = self.move(nums, n, i+1, memo)
        
        best = max(rob_this_house, rob_next_house)
        
        for j in range(i+2, n):
            amount = self.move(nums, n, j, memo)
            if amount + rob_this_house > best:
                best = amount + rob_this_house 
                
        memo[i] = best
        return memo[i]
        
    def small_rob(self, nums):
        memo = {}
        
        self.move(nums, len(nums), 0, memo)
        
        best = 0
        for k,v in memo.items():
            best = max(best, v)
        return best
    
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        return max(self.small_rob(nums[1:]), self.small_rob(nums[:-1]))

s = Solution()

nums = [1,2,3,1] # expct 4
print(s.rob(nums))