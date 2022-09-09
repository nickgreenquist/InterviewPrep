class Solution:      
    def change(self, amount, coins):
        memo = {}
        for i in range(amount + 1):
            memo[i] = 0
        memo[0] = 1 # if i - amount reaches 0, that's 1 path
        
        # unbounded knapsack: outerloop is every coin to remove dupes
        for coin in coins:
            for i in range(amount + 1):
                if i - coin >= 0: 
                    memo[i] = memo[i] + memo[i-coin]
                    
        return memo[amount]

'''
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
'''
s = Solution()
print(s.change(5, [1,2,5]))