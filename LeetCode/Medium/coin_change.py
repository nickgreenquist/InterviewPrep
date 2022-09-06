
def coinChange(coins, amount):
    lookup = {}
    for i in range(amount + 1):
        lookup[i] = float('inf')
    lookup[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                lookup[i] = min(lookup[i], lookup[i - coin] + 1)
                
    if lookup[amount] <= amount:
        return lookup[amount]
    return -1
'''
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
'''
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))

# Recursive solution
class Solution:
    def change(self, coins, num_coins, amount,  memo):
        if amount < 0:
            return 100000
        if amount in memo:
            return memo[amount]
            
        memo[amount] = 100000
        for coin in coins:
            can = self.change(coins, num_coins + 1, amount - coin, memo)
            memo[amount] = min(memo[amount], can + 1)
            
        return memo[amount]
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0] = 0
        
        coins = sorted(coins, reverse=True)
        
        self.change(coins, 0, amount, memo)
        
        # memo[i] = least num of coins need to make amount i
        if memo[amount] != 100000:
            return memo[amount]
        else:
            return -1
