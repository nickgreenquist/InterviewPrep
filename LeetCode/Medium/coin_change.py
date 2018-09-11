
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
