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


# Another O(N^2) solution using two pointer bubble from middle approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
    
        res_L = 0
        res_R = 0
        res_len = 0
        
        for i in range(len(s)):
            # check odd length
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome_len = right - left + 1
                if palindrome_len > res_len:
                    res_len = palindrome_len
                    res_L = left
                    res_R = right
                left -= 1
                right += 1
            
            # check even length
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome_len = right - left + 1
                if palindrome_len > res_len:
                    res_len = palindrome_len
                    res_L = left
                    res_R = right
                left -= 1
                right += 1
        
        return s[res_L:res_R+1]
