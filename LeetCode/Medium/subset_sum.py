def subset_sum(nums, amount):
    dp = []
    for i in range(len(nums)):
        dp.append([])
        for j in range(amount + 1):
            dp[i].append(False)
    
    for i in range(len(nums)):
        for j in range(amount + 1):
            if j - nums[i] == 0:
                dp[i][j] = True
            else:
                dp[i][j] = False
                
                if i-1 >= 0:
                    skip = dp[i-1][j]
                    use = False
                    if j - nums[i] >= 0:
                        use = dp[i-1][j - nums[i]]
                    dp[i][j] = use or skip
    
    for i in range(len(nums)):
        if dp[i][amount]:
            return True
    return False

nums = [5, 1, 12, 5]
amount = 11
print(subset_sum(nums, amount))