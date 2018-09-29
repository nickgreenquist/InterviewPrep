def isValid(s):
    left = []
    right = []
    for c in s:
        if c in {'(', '[', '{'}:
            left.append(c)
        if c in {')', ']', '}'}:
            if not left:
                return False
            l = left.pop()
            if l == '(' and c != ')':
                return False
            if l == '[' and c != ']':
                return False
            if l == '{' and c != '}':
                return False
    if left:
        return False
    return True
'''
Example 1:
Input: "()"
Output: true
'''
print(isValid("()"))

'''
Example 2:
Input: "()[]{}"
Output: true
'''
print(isValid("()[]{}"))

'''
Example 3:
Input: "(]"
Output: false
'''
print(isValid("(]"))

'''
Example 4:
Input: "([)]"
Output: false
'''
print(isValid("([)]"))

'''
Example 5:
Input: "{[]}"
Output: true
'''
print(isValid("{[]}"))
