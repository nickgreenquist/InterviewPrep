'''
Given an arithmetic equation consisting of positive integers,+,-,* and/ (no parentheses), compute the result. 

EXAMPLE Input: 2*3+5/6*3+15
Output: 23.5
'''

def calc(exp):
    nums = []
    ops = []
    curr_num = ''

    # go through and split expression into numbers and operators
    for i in range(len(exp)):
        if exp[i] in '*+-/':
            nums.append(int(curr_num))
            curr_num = ''
            ops.append(exp[i])
        else:
            curr_num += exp[i]
    # add the final number
    nums.append(int(curr_num))

    # Handle multiplication and division
    i = 0
    while i < len(ops):
        if ops[i] in '*/':
            if ops[i] == '*':
                result = nums[i] * nums[i+1]
            else:
                result = nums[i] / nums[i+1]
            del ops[i]
            del nums[i]
            del nums[i]
            nums.insert(i, result)
        else:
            i += 1
    
    # Handle addition and subtraction
    i = 0
    while i < len(ops):
        if ops[i] == '+':
            result = nums[i] + nums[i+1]
        else:
            result = nums[i] + nums[i+1]
        del ops[i]
        del nums[i]
        del nums[i]
        nums.insert(i, result)

    return nums[0]


exp = '2*3+5/6*3+15'
print(calc(exp))