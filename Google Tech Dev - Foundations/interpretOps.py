'''
Write a simple interpreter which understands "+", "-", and "*" 
operations. Apply the operations in order using command/arg pairs 
starting with the initial value of `value`. If you encounter an unknown command, return -1.
'''

def interpret(total, ops, vals):
    if len(ops) != len(vals):
        return None
    for i in range(len(ops)):
        op = ops[i]
        val = vals[i]
        if op == '+':
            total += val
        elif op == '*':
            total *= val
        elif op == '-':
            total -= val
        elif op == '/':
            total /= val
    return total


print(interpret(1, ["+"], [1])) # 2
print(interpret(4, ["-"], [2])) # 2
print(interpret(1, ["+", "*"], [1, 3])) # 6