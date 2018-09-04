class Permuter(object):
    output = []
    buf = []
    def permall(self, nums):
        # used all from input list
        if len(self.buf) == len(nums):
            temp = self.buf[:]
            self.output.append(temp)
            return
        
        # go through list and find next available number to use
        for i in range(0, len(nums)):
            if nums[i] in self.buf:
                continue
                
            # the 'important' part
            self.buf.append(nums[i])
            self.permall(nums)
            del self.buf[len(self.buf) - 1]
        
    def permute(self, nums):
        self.output = []
        self.buf = []
        self.permall(nums)
        return self.output

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
permuter = Permuter()
print(permuter.permute(nums))