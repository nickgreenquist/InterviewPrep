def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    
    # Build table K[][] in bottom up manner 
    for i in range(n+1):
        for w in range(W+1):
            # 0 value for no items or no weight
            if i == 0 or w == 0:
                K[i][w] = 0
            
            # if this item can fit in knapsack
            elif wt[i-1] <= w:
                # if the value of this item plus the best total value
                # from the last item minus this item's weight
                if K[i-1][w] < K[i-1][w - wt[i-1]] + val[i-1]:
                    K[i][w] = K[i-1][w - wt[i-1]] + val[i-1]
                else:
                    # the best value at this item and weight is the best value
                    # from the last item with this weight
                    K[i][w] = K[i-1][w]
            else:
                K[i][w] = K[i-1][w]
        
    # the highest value would bubble up to here
    return K[n][w]

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