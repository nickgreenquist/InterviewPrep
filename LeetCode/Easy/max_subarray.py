'''
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def maxSubArray(nums):
        """
        Returns max sum of any subarray in nums
        """
        sum = 0
        max_sum = float('-inf')
        for num in nums:
            if sum == 0 and num < 0:
                max_sum = max(max_sum, num)
            else:
                sum += num
                max_sum = max(max_sum, sum)
                if sum < 0:
                    sum = 0
        return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))