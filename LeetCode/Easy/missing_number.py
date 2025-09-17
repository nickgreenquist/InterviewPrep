def missingNumber(nums):
    x = 0
    for i in range(len(nums)+1):
        x = x ^ i
    for i in range(len(nums)):
        x = x ^ nums[i]
    return x  

nums = [3,0,1]
print(missingNumber(nums))