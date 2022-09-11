class Solution:
    
    def isValley(self, prices, i):
        if i == len(prices) - 1:
            return False
        if i == 0:
            return prices[i] < prices[i + 1]
        
        if prices[i] < prices[i + 1] and prices[i] <= prices[i - 1]:
            return True
        return False
    
    def isPeak(self, prices, i):
        if i == len(prices) - 1:
            return prices[i] > prices[i-1]
        if i == 0:
            return False
        if prices[i] >= prices[i + 1] and prices[i] > prices[i - 1]:
            return True
        return False
        
    # buy at valleys, sell at peaks
    def maxProfit(self, prices):
        profit = 0
        
        for i in range(len(prices)):
            if self.isValley(prices, i):
                profit -= prices[i]
            else:
                if self.isPeak(prices, i):
                    profit += prices[i]
                
        return profit

'''
Input: prices = [7,1,5,3,6,4]
Output: 7
'''
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))