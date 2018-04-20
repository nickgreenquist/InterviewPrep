def non_repeating(s):
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    for key,value in count.items():
        if value == 1:
            return key
    return None

print(non_repeating('aabcc'))
print(non_repeating('xxyz'))
print(non_repeating('aabb'))