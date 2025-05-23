def scoreOfString(s):
    """
    :type s: str
    :rtype: int
    """
    out = 0
    for i in range(len(s) - 1):
        out += abs(ord(s[i]) - ord(s[i+1]))

    return out

print(scoreOfString("hello")) # 13
print(scoreOfString("zaz")) # 50