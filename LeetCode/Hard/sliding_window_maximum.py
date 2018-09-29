'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.
'''
def maxSlidingWindow(nums, k):
    if not nums:
        return []
    
    indices = []
    best = float('-inf')
    best_i = 0
    for i in range(k):
        indices.append(i)
        if nums[i] > best:
            best = nums[i]
            best_i = i
            
    # trim all suboptimal numbers less than and to the left of the first window best
    j = 0
    while j < len(indices):
        if indices[j] < best_i and nums[indices[j]] < best:
            indices.pop(j)
            j -= 1
        j += 1
    
    out = [best]
    for i in range(k, len(nums)):
        if indices[0] <= i - k:
            indices.pop(0)
            
        # trim all suboptimal indices in the current list
        j = 0
        while j < len(indices):
            if nums[indices[j]] < nums[i]:
                indices.pop(j)
                j -= 1
            j += 1
        indices.append(i)
        out.append(nums[indices[0]])
    return out
'''
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 '''
print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))