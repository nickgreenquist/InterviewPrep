def buildFromPattern(pattern, main, alt):
    ans = ""
    first = pattern[0]
    for c in pattern:
        if c == first:
            ans += main
        else:
            ans += alt
    return ans

def match(pattern, value):
    for i in range(0, len(value)):
        main = value[0:i]
        for j in range(i, len(value) + 1):
            for k in range(j, len(value) + 1):
                alt = value[j:k]
                cand = buildFromPattern(pattern, main, alt)
                if cand == value:
                    return True
    return False

pattern = 'ab'
value = 'catcatgocatgo'
print( match(pattern, value))