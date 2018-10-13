'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.

Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.
'''

def buildTree(nums, i, current, S, seen):
    if i >= len(nums):
        if current == S:
            return 1
        return 0
    
    if (i, current) in seen:
        return seen[(i, current)]
    seen[(i, current)] = buildTree(nums, i+1, current + nums[i], S, seen) + buildTree(nums, i+1, current - nums[i], S, seen)
    return seen[(i, current)]
        
def findTargetSumWays(nums, S):
    seen = {}
    return buildTree(nums, 0, 0, S, seen)

'''
Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
'''
print(findTargetSumWays(nums = [1, 1, 1, 1, 1], S = 3))