'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
and all letters reverse their positions.
'''

def reverseOnlyLetters(S):
    # turn string to list of chars because you can't
    # swap chars in a string with each other
    arr = [c for c in S]

    i = 0
    j = len(arr) - 1
    while i < j:
        if not arr[i].isalpha() and not arr[j].isalpha():
            i += 1
            j -= 1
        elif not arr[i].isalpha():
            i += 1
        elif not arr[j].isalpha():
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return "".join(arr)

'''
Example 1:
Input: "ab-cd"
Output: "dc-ba"
'''
inp = "ab-cd"
print("{}: {}\n".format(inp, reverseOnlyLetters(inp)))

'''
Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
'''
inp = "a-bC-dEf-ghIj"
print("{}: {}\n".format(inp, reverseOnlyLetters(inp)))

'''
Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
'''
inp = "Test1ng-Leet=code-Q!"
print("{}: {}\n".format(inp, reverseOnlyLetters(inp)))
