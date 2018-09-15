def containsDuplicate(nums):
    return len(nums) != len(set(nums))

'''
Input: [1,2,3,1]
Output: true
'''
print(containsDuplicate([1,2,3,1]))

'''
Input: [1,2,3,4]
Output: false
'''
print(containsDuplicate([1,2,3,4]))