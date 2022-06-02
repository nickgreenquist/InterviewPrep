def productExceptSelf(nums):
    if len(nums) <= 1:
        return nums

    output = [1] * len(nums)
    i = len(nums) - 2
    m = nums[i + 1]
    while i >= 0:
        output[i] = m
        m *= nums[i]
        i -= 1
    
    # output now contains all products from right of num at index
    # now we want to mult with products from left of num at index
    i = 1
    m = nums[0]
    while i < len(nums):
        output[i] = output[i] * m
        m *= nums[i]
        i += 1
    
    return output

nums = [1, 2, 3, 4]
output = productExceptSelf(nums)
print(output)