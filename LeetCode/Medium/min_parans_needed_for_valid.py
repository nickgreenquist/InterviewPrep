def minAddToMakeValid(S):
    needed = 0
    lefts = 0
    for c in S:
        if c == '(':
            lefts += 1
        if c == ')':
            if lefts < 1:
                needed += 1
            else:
                lefts -=1
    return needed + lefts

'''
Example 1:
Input: "())"
Output: 1
'''
print(minAddToMakeValid("())"))

'''
Example 2:
Input: "((("
Output: 3
'''
print(minAddToMakeValid("((("))

'''
Example 3:
Input: "()"
Output: 0
'''
print(minAddToMakeValid("()"))

'''
Example 4:
Input: "()))(("
Output: 4
'''
print(minAddToMakeValid("()))(("))
