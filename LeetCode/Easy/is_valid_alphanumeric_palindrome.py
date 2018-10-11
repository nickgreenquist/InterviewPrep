'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
'''
def isPalindrome(s):
    i = 0
    j = len(s) - 1
    s = s.lower()
    while i < j:
        if not s[i].isalpha() and not s[i].isnumeric():
            i += 1
        elif not s[j].isalpha() and not s[j].isnumeric():
            j -= 1
        elif s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

'''
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
'''
s = "A man, a plan, a canal: Panama"
print("{}: {}".format(s, isPalindrome(s)))

'''
Example 2:

Input: "race a car"
Output: false
'''
s = "race a car"
print("{}: {}".format(s, isPalindrome(s)))