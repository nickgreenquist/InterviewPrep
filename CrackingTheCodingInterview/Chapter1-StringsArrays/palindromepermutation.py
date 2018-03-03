def palinperm(s):
    d = {}
    s = s.lower()
    s = s.replace(" ", "")
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    numOdd = 0
    for v in d.values():
        if v % 2 != 0:
            numOdd += 1
    if numOdd > 1:
        return False
    return True

s = 'Tact Coay'
print(palinperm(s))
