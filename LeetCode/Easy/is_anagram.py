def isAnagram(s, t):
    char_set_s = sorted([c for c in s])
    char_set_t = sorted([c for c in t])
    return char_set_s == char_set_t

'''
Input: s = "anagram", t = "nagaram"
Output: true
'''
s = 'anagram'
t = 'nagaram'
print(isAnagram(s, t))