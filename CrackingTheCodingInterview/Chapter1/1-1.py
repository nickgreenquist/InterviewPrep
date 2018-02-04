
def isUnique(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True

def isUniqueNoDict(s):
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

s = 'abcde'
print( isUniqueNoDict(s))