
def largestRectangleArea(height):
    height.append(0) # this will force us to end easily
    stack = [-1]
    best = 0
    for i in range(len(height)):
        # while this height is less than height at top of the stack
        while height[i] < height[stack[-1]]:
            # get the height of the top of the stack's bar
            top_height = height[stack.pop()]
            
            # width is this index minus the index of the top of the stack's bar
            width = i - stack[-1] - 1
            
            
            best = max(best, top_height * width)
        
        # add this bar into stack once all higher previous bars have been dealt with
        stack.append(i)
    height.pop()
    return best

'''
Input: [2,1,5,6,2,3]
Output: 10
'''
heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))