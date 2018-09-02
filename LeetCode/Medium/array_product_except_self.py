
def productExceptSelf(nums):
    output = [1] * len(nums)
    i = len(nums) - 2
    while i >= 0:
        output[i] *= output[i + 1] * nums[i + 1]
        i -= 1
    i = 1
    m = 1
    while i < len(nums):
        m *= nums[i - 1]
        output[i] *= m
        i += 1
    return output

'''
Input:  [1,2,3,4]
Output: [24,12,8,6]
'''
print(productExceptSelf([1,2,3,4]))
