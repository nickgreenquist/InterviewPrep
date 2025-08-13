def maxProduct(nums):
    max_so_far = nums[0]
    min_so_far = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        new_max = max(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
        new_min = min(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
        
        best = max(new_max, best)

        max_so_far = new_max
        min_so_far = new_min
    return best
    
    

'''
Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180

Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
'''

nums = [-2, 6, -3, -10, 0, 2]
solution = maxProduct(nums)

print(solution)