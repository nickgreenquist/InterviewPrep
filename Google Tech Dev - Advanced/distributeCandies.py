'''
Given an integer array with even length, 
where different numbers in this array represent 
different kinds of candies. Each number means 
one candy of the corresponding kind. 
You need to distribute these candies equally in 
number to brother and sister. Return the maximum 
number of kinds of candies the sister could gain.
'''

def distributeCandies(candies):
        unique = set()
        for c in candies:
            unique.add(c)
        
        return min(len(candies) // 2, len(unique))

candies = [1,1,2,2,3,3]
print(distributeCandies(candies)) # 3

candies = [1,1,2,3]
print(distributeCandies(candies)) # 2