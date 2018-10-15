'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
'''

def maxProfit(prices):   
    min_val = float('inf')
    best_trade = 0
    for num in prices:
        if num - min_val > 0:
            best_trade = max(best_trade, num - min_val)
        min_val = min(min_val, num)
    
    return best_trade

'''
Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
'''
print(maxProfit([7,1,5,3,6,4]))


'''
Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
print(maxProfit([7,6,4,3,1]))