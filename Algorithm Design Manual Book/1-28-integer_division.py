'''
Write a function to perform integer division without using either the / or *
operators. Find a fast way to do it.
'''

def div_basic(x, y):
    i = 0
    sum = y

    while sum < x:
        sum += y
        i += 1
    return i

def is_neg_result(x, y):
    if x < 0 and y < 0:
        return False
    if x < 0 or y < 0:
        return True
    return False

def div(dividend, divisor):
    if divisor == 0:
        return None
    
    res = 1
    denominator = divisor
    last_denominator = divisor
    last_result = res

    # Double denominator value with bitwise shift until bigger than dividend
    while dividend > denominator:
        last_denominator = denominator
        last_result = res

        denominator <<= 1
        res <<= 1

    # After we overstep, check if we are closer now to final dividend (substract until we get there)
    # or last iteration was closer (add until we get there)

    if (abs(denominator - dividend) <= abs(last_denominator - dividend)):
        # Subtract divisor value until denominator is smaller than dividend
        while denominator > dividend:
            denominator -= divisor
            res -= 1
    else:
        # Add divisor value until denominator is greater than dividend
        res = last_result
        denominator = last_denominator

        while denominator < dividend:
            denominator += divisor
            res += 1
            if (denominator > dividend): # correct final overstep
                res -= 1

    if is_neg_result(dividend, divisor):
        res = -res

    return res


for i in range(1000):
    for j in range (100):
        if j == 0:
            continue
        if div(i, j) != i // j:
            t = div(i, j)
            print("WRONG")
    