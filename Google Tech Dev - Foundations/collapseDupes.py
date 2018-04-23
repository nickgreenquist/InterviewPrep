
def collapseDuplicates(a):
    i = 0
    result = ""
    while i < len(a):
        ch = a[i]
        result += ch
        while i < len(a) - 1 and a[i+1] == ch:
            i += 1
        i += 1
    return result

print(collapseDuplicates("a")) # "a"
print(collapseDuplicates("aa")) # "a"
print(collapseDuplicates("abc")) # "abc"