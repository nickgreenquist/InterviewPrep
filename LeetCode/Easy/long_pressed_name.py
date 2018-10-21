'''
Your friend is typing his name into a keyboard.
Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.
Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
'''
def isLongPressedName(name, typed):
    tups_typed = []
    i = 0
    while i < len(typed):
        count = 1
        j = i + 1
        while j < len(typed) and typed[j] == typed[i]:
            j += 1
            count += 1
        tups_typed.append((typed[i], count))
        count = 0
        i = j
    
    tups_name = []
    i = 0
    while i < len(name):
        count = 1
        j = i + 1
        while j < len(name) and name[j] == name[i]:
            j += 1
            count += 1
        tups_name.append((name[i], count))
        count = 0
        i = j
    
    if len(tups_typed) != len(tups_name):
        return False
    for i in range(len(tups_typed)):
        if tups_typed[i][0] != tups_name[i][0] or tups_typed[i][1] < tups_name[i][1]:
            return False
    return True

'''
Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
'''
print(isLongPressedName(name = "alex", typed = "aaleex"))

'''
Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
'''
print(isLongPressedName(name = "saeed", typed = "ssaaedd"))

'''
Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true
'''
print(isLongPressedName(name = "leelee", typed = "lleeelee"))

'''
Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
'''
print(isLongPressedName(name = "laiden", typed = "laiden"))