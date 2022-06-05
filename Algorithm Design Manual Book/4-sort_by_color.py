class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        j = n - 1
        
        # first, put all non-0's to the back
        while i <= j:             
            if nums[i] != 0:
                self.swap(nums, i, j)
                j -= 1
            else:
                i += 1
        
        # next, from where we left off after moving all 0's, 
        # put all non-1's to the back
        j = n - 1
        while i <= j:       
            if nums[i] != 1:
                self.swap(nums, i, j)
                j -= 1
            else:
                i += 1

nums = [2,0,2,1,1,0]
s = Solution()
s.sortColors(nums)
print(nums)