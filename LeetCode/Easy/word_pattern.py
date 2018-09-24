def wordPattern(pattern, str):
    to_match = []
    for c in pattern:
        to_match.append(c)
    words = str.split()
    if len(words) != len(to_match):
        return False
    mapper = {}
    used = set()
    for i in range(len(to_match)):
        c = to_match[i]
        if c not in mapper:
            if words[i] in used:
                return False
            mapper[c] = words[i]
            used.add(words[i])
        else:
            if words[i] != mapper[c]:
                return False
    return True

'''
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Input: pattern = "abba", str = "dog cat cat fish"
Output: false

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
'''

print(wordPattern(pattern = "abba", str = "dog cat cat dog"))
print(wordPattern(pattern = "abba", str = "dog cat cat fish"))
print(wordPattern(pattern = "abba", str = "dog dog dog dog"))
