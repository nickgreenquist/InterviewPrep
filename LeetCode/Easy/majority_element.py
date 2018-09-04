def majorityElement(nums):
        candidate = -1
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    candidate = num
                    count = 1
        
        return candidate

'''
Input: [2,2,1,1,1,2,2]
Output: 2
'''
print(majorityElement([2,2,1,1,1,2,2]))