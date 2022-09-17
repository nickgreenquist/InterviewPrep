def knapSack(W, wt, val, n):
    dp = []
    for i in range(n+1):
        dp.append([])
        for j in range(W+1):
            dp[i].append(0)
    
    # bottom up knapsack
    for i in range(n+1):
        for w in range(W+1):
            # base case
            if i == 0 or w == 0:
                dp[i][w] = 0
                continue
            
            # if wt[i-1] doesn't fit into curent weight limit
            if wt[i-1] > w:
                dp[i][w] = dp[i-1][w]
                continue
            
            # if the value of this item plus the best total value
            # from the last item minus this item's weight is better
            # than best total value from last item at this weight limit
            if val[i-1] + dp[i-1][w - wt[i-1]] > dp[i-1][w]:
                dp[i][w] = val[i-1] + dp[i-1][w - wt[i-1]]
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]


# Driver program to test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print("Expected: {}, Returned: {}".format(220, knapSack(W, wt, val, n)))

val = [20,5,10,40,15,25]
wt = [1,2,3,8,7,4]
W = 10
n = len(val)
print("Expected: {}, Returned: {}".format(60, knapSack(W, wt, val, n))) 