def findPermutationDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    c_to_i = {}
    for i in range(len(s)):
        c_to_i[s[i]] = i
    
    total = 0
    for i in range(len(t)):
        total += abs(i - c_to_i[t[i]])
    return total

'''
Input: s = "abcde", t = "edbac"
Output: 12
'''
s = "abcde"
t = "edbac"
print(findPermutationDifference(s, t) == 12)