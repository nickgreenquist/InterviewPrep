def cut(n, prices, memo):
    if n == 1:
        return prices[0]
    if n in memo:
        return memo[n]
    
    # enumarate all possible cuts with rod length n
    best_profit = 0
    for keep in range(n, 1, -1):
        split = n - keep
        if split not in memo:
            memo[split] = cut(split, prices, memo)

        profit = prices[keep] + memo[split]
        if profit > best_profit:
            best_profit = profit

    memo[n] = best_profit
    return memo[n]

n = 5
prices = [0,1,5,8,9,10] # best is cut [2..3] profit = 13

memo = {}
memo[0] = 0 # empty rod, 0 profit

cut(n, prices, memo)
print(memo[n])