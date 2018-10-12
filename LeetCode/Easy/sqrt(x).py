def sqrt(x):
    if x < 0:
        return None
    elif x == 0:
        return 0
    else:
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r

print(sqrt(8))