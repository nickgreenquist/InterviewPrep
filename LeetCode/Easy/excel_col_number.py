'''
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
'''

def titleToNumber(s):
    base = 1
    tot = 0
    for i in range(len(s) - 1, -1, -1):
        val = ord(s[i]) - ord('A') + 1
        tot += (val * base)
        base *= 26
    return tot

inp = 'ZY'
print(titleToNumber(inp))