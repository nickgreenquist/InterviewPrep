class Solution:
    def perm(self, nums, L, R):
        if L == R:
            self.results.append(nums[:])
        else:
            for i in range(L, R):
                nums[i], nums[L] = nums[L], nums[i]
                self.perm(nums, L + 1, R)
                nums[i], nums[L] = nums[L], nums[i]
        
    def permute(self, nums):
        self.results = []
        self.perm(nums, 0, len(nums))
        return self.results

'''
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
nums = [1,2,3]
permuter = Solution()
print(permuter.permute(nums))