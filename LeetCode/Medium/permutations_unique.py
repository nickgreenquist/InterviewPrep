class Solution:
    def perm(self, nums, L, R):
        if L == R:
            self.results.append(nums[:])
        else:
            used = set()
            for i in range(L, R):
                if nums[i] not in used:
                    used.add(nums[i])
                    nums[i], nums[L] = nums[L], nums[i]
                    self.perm(nums, L + 1, R)
                    nums[i], nums[L] = nums[L], nums[i]
        
    def permuteUnique(self, nums):
        self.results = []
        self.perm(nums, 0, len(nums))
        return self.results

'''
Input: nums = [1,1,2]
Output:
[
    [1,1,2],
    [1,2,1],
    [2,1,1]
]
'''
nums = [1,1,2]
permuter = Solution()
print(permuter.permuteUnique(nums))