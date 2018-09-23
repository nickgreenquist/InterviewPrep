'''
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.
Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.
'''
def findLongestChain(pairs):
    current = float('-inf')
    result = 0
    pairs = sorted(pairs, key=lambda x: x[1])
    for pair in pairs:
        if current < pair[0]:
            current = pair[1]
            result += 1
    return result
'''
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
'''
print(findLongestChain([[1,2], [2,3], [3,4]]))
