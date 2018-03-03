def printBinary(num):
    if num < 0 or num > 1:
        return "ERROR"

    binary = "."
    while num > 0:
        print(binary)
        if len(binary) > 32:
            return "ERROR"

        r = num * 2
        if r >= 1:
            binary += "1"
            num = r - 1
        else:
            binary += "0"
            num = r
    return binary

print( printBinary(0.6) )