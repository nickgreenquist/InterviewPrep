'''
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
'''

def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    max_candies = max(candies) - extraCandies
    return [num_candy >= max_candies for num_candy in candies]

'''
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
'''
candies = [2,3,5,1,3]
extraCandies = 3
expected = [True,True,True,False,True] 
print(kidsWithCandies(candies, extraCandies) == expected)