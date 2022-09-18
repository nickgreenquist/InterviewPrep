class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
    
        count = 0
        
        for i in range(len(s)):
            # check odd length
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            # check even length
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        return count

'''
Input: s = "aaa"
Output: 6
'''

s = Solution()
print(s.countSubstrings("aaa"))