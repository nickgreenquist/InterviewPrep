
'''
Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''

class FindDifferenceSolution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        valid = {}
        for c in s:
            if c in valid:
                valid[c] += 1
            else:
                valid[c] = 1
        for c in t:
            if c not in valid:
                return c
            valid[c] -= 1
            if valid[c] < 0:
                return c
s = "abcd"
t = "abcde"
print(FindDifferenceSolution().findTheDifference(s,t))