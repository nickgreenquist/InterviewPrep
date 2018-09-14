def plusOne(digits):
    i = len(digits) - 1
    carry = 1
    while i >= 0:
        digits[i] += carry
        carry = 0
        
        if digits[i] == 10:
            digits[i] = 0
            carry = 1
            
        i -= 1
        
    if carry:
        digits.insert(0, carry)
    return digits

'''
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
print(plusOne([4,3,2,1]))
print(plusOne([9,9,9]))