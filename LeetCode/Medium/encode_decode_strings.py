from typing import List

'''
Idea: pick a delimiter and also add the length of chars to encode
str(len(s1)) + '#' + s1 + str(len(s2)) + '#' +  s2 + ...
'''

def encode(strs: List[str]) -> str:
    res = ''
    for s in strs:
        res += str(len(s)) + '#' + s
    return res

def decode(s: str) -> List[str]:
    def decodeLen(i):
        num_str = ''
        while s[i] != '#':
            num_str += s[i]
            i += 1
        return int(num_str), i + 1

    res = []

    num, i = decodeLen(0)
    while i < len(s):
        res.append(s[i:i+num])
        i += num
        if i < len(s):
            num, i = decodeLen(i)
        else:
            break
        
    return res
        


'''
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

4#neet4#code#4love#3you
'''

strings = ["neet","code","love","you"]
print(strings)
encoded = encode(strings)
print(encoded)
decoded = decode(encoded)
print(decoded)