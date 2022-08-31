class Solution:
    def sub(self, nums, subset, k):
        if k >= len(nums):
            self.result.append(subset.copy())
            return
        
        # include nums[k] in subset
        subset.append(nums[k])
        self.sub(nums, subset, k + 1)
        
        # do not include nums[k]
        subset.pop()
        self.sub(nums, subset, k + 1)
        
    def subsets(self, nums):
        self.result = []
        
        self.sub(nums, [], 0)
        
        return self.result

'''
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
s = Solution()
print(s.subsets([1,2,3]))