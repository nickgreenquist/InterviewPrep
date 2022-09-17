def knapSack(W, wt, val, n):
    pass


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