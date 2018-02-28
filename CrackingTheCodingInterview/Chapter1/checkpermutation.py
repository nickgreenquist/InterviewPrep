def checkPerm(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_dic = {}
    for c in s1:
        if c in s1_dic:
            s1_dic[c] += 1
        else:
            s1_dic[c] = 1
    
    for c in s2:
        if c not in s1_dic:
            return False
        else:
            if s1_dic[c] == 0:
                return False
            else:
                s1_dic[c] -= 1
    return True

s1 = 'abcde'
s2 = 'ebacu'

print( checkPerm(s1, s2))
        