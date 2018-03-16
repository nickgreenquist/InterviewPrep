def add(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    
    sum = a ^ b # add without carrying
    carry = (a & b) << 1 # carry but not add

    print("Sum: %s, Carry: %s" % (sum, carry))
    return add(sum, carry)


a = 5
b = 6
sum = add(a, b)
print(sum)