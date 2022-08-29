class Solution:
    def twoSum(self, nums, target, index_to_ignore):
        A = {}
        for i in range(0, len(nums)):
            if i == index_to_ignore:
                continue
                
            val = target - nums[i]
            if val in A:
                A[val].append(i)
            else:
                A[val] = [i]
        
        results = []
        seen_doubles = set()
        for i in range(len(nums)):
            if i == index_to_ignore:
                continue
                
            num = nums[i]
            if num in A:
                indices = A[num]
                # if only one number has num as diff, check if it is itself
                if len(indices) == 1:
                    if indices[0] == i:
                        continue
                    else:
                        double = sorted([nums[i], nums[indices[0]]])
                        sorted_indices_set_key = ','.join([str(x) for x in double])
                        if sorted_indices_set_key not in seen_doubles:
                            results.append(double)
                            seen_doubles.add(sorted_indices_set_key)
                else:
                    # return first index that is not yourself
                    for index in indices:
                        if index != i:
                            double = [nums[i], nums[index]]
                            sorted_indices_set_key = ','.join([str(x) for x in double])
                            if sorted_indices_set_key not in seen_doubles:
                                results.append(double)
                                seen_doubles.add(sorted_indices_set_key)
                
        return results
    
    def threeSum(self, num):
        counts = {}
        trimmed = []
        for num in nums:
            if num not in counts:
                counts[num] = 0
                
            if counts[num] < 3:
                trimmed.append(num)
                counts[num] += 1
        
        target = 0
        results = []
        seen_triplets = set()
        
        for i in range(len(trimmed)):
            val = target - trimmed[i]
            two_sums = self.twoSum(trimmed, val, i)
            for two_sum in two_sums:
                triplet = sorted([two_sum[0], two_sum[1], trimmed[i]])
                sorted_indices_set_key = ','.join([str(x) for x in triplet])
                if sorted_indices_set_key not in seen_triplets:
                    results.append(triplet)
                    seen_triplets.add(sorted_indices_set_key)
        return results

'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

nums = [-1,0,1,2,-1,-4]
threeSum = Solution()
print(threeSum.threeSum(nums))