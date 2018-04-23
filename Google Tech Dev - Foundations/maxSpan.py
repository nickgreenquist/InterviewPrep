'''
Consider the leftmost and righmost appearances of some value in an array. 
We'll say that the "span" is the number of elements between the two inclusive. 
A single value has a span of 1. Returns the largest span found in the given array. 
(Efficiency is not a priority.)
'''

def max_span(arr):
    leftmost = {}
    rightmost = {}
    maxspan = 0
    for i in range(len(arr)):
        n = arr[i]
        if n not in leftmost:
            leftmost[n] = i
        else:
            rightmost[n] = i
            maxspan = max(maxspan, rightmost[n] - leftmost[n] + 1)
    return maxspan

print(max_span([1, 2, 1, 1, 3])) # 4
print(max_span([1, 4, 2, 1, 4, 1, 4])) # 6
print(max_span([1, 4, 2, 1, 4, 4, 4])) # 6
    
