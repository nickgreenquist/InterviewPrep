def isNum(c):
    try:
        float(c)
        return True
    except:
        return False
    
def myAtoi(str):
    str = str.strip()
    
    if len(str) < 1:
        return 0
    
    negate = False
    low = 0
    i = 0
    
    if str[i] == '-' or str[i] == '+':
        if str[i] == '-':
            negate = True
        i += 1
        low = 1
        
    if i < len(str) and isNum(str[i]):
        
        # read in valid integer
        while i < len(str) and isNum(str[i]):
            i += 1
        i -= 1
        
        num = 0
        base = 0      
        while i >= low:
            num += pow(10, base)*int(str[i])
            i -= 1
            base += 1

        if negate:
            num = -num
        
        # check for overflow
        if num < -2147483648:
            return -2147483648      
        if num > 2147483647:
            return 2147483647
        
        return num
    else:
        return 0

'''
Example 1:
Input: "42"
Output: 42
'''
print(myAtoi("42"))

'''
Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
'''
print(myAtoi("   -42"))

'''
Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
'''
print(myAtoi("4193 with words"))

'''
Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
'''
print(myAtoi("words and 987"))

'''
Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
'''
print(myAtoi("-91283472332"))