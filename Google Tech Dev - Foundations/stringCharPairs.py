'''
Given an array of non-empty strings, create and return a Map<String, String> as follows: 
for each string add its first character as a key with its last character as the value.
'''

def pairs(words):
    d = {}
    for word in words:
        d[word[0]] = word[-1]
    return d

print(pairs(["code", "bug"])) # {"b": "g", "c": "e"}
print(pairs(["man", "moon", "main"])) # {"m": "n"}
print(pairs(["man", "moon", "good", "night"])) # {"g": "d", "m": "n", "n": "t"}