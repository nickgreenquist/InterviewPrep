'''
Given a string, return the sum of the numbers appearing in the string, 
ignoring all other characters. A number is a series of 1 or more digit chars in a row. 
(Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. 
Integer.parseInt(string) converts a string to an int.)
'''

def string_to_num(s):
    s = s[::-1]
    base = 0
    num = 0
    for c in s:
        num += int(c) * 10**base
        base += 1
    return num

def sum_numbers(s):
    sum = 0
    num = ''
    for c in s:
        if c.isdigit():
            num += c
        else:
            if len(num) > 0:
                sum += string_to_num(num)
            num = ''
    if len(num) > 0:
        sum += string_to_num(num)
    return sum

print(sum_numbers("abc123xyz")) # 123
print(sum_numbers("aa11b33")) # 44
print(sum_numbers("7 11")) # 18
