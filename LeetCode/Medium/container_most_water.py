'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''
def maxArea(height):
    n = len(height)
    best = 0
    i = 0
    j = n-1
    while i <= j:
        best = max(best, min(height[i], height[j]) * (j-i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return best
'''
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
print(maxArea([1,8,6,2,5,4,8,3,7]))
