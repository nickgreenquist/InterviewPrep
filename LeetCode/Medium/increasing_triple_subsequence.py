def increasingTriplet(nums):
    if len(nums) < 3:
        return False
    lowest = float('inf')
    second_lowest = float('inf')
    
    for num in nums:
        if num <= lowest:
            lowest = num
        elif num <= second_lowest:
            second_lowest = num
        elif num > second_lowest:
            return True
        
    return False

'''
Example 1:
Input: [1,2,3,4,5]
Output: true
'''
print(increasingTriplet([1,2,3,4,5]))

'''
Example 2:
Input: [1,1,-6,2]
Output: false
'''
print(increasingTriplet([1,1,-6,2]))