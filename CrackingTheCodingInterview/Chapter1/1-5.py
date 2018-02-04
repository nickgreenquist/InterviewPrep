def oneaway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    big = ""
    small = ""
    if len(s1) > len(s2):
        big = s1
        small = s2
    else:
        big = s2
        small = s1
    
    edits = 0
    i = 0
    j = 0
    while i < len(big) and j < len(small):
        if big[i] != small[j]:
            edits += 1
            if len(big) == len(small):
                j += 1
        else:
            j += 1
        i += 1
    return edits <= 1
        

print( oneaway('bake', 'ple'))
        