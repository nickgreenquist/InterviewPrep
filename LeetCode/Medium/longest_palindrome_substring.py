'''
Given a string s, find the longest palindromic substring in s.
'''

def longestPalindrome(s):
    n = len(s)
    ans = ""
    lookup = [[False]*n for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            # if characters match and they are at most 2 away
            if s[i] == s[j] and (j - i <= 2 or lookup[i+1][j-1]):
                lookup[i][j] = True
            else:
                lookup[i][j] = False
                
            # if valid palindrome here and either the current answer is null or
            # current length of this palindrome range is longer than the answer
            if lookup[i][j] and (len(ans) < 1 or j - i + 1 > len(ans)):
                ans = s[i:j+1]
    return ans

'''
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''
print(longestPalindrome("babad"))

'''
Example 2:
Input: "cbbd"
Output: "bb"
'''
print(longestPalindrome("cbbd"))
