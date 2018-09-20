def missingNumber(nums):
    x = 0
    i = 0
    while i < len(nums):
        num = nums[i]
        x = x ^ i ^ num
        i += 1
    x = x ^ i
    return x

print(missingNumber([3, 0, 1, 4, 5, 6]))