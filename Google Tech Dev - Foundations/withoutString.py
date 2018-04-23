'''
Given two strings, base and remove, return a version of the base string 
where all instances of the remove string have been removed (not case sensitive). 
You may assume that the remove string is length 1 or more. 
Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".
'''

def without_string(base, remove):
    # sliding window approach
    i = 0
    while i < len(base) - len(remove):
        found = True
        for j in range(len(remove)):
            if base[j + i] != remove[j]:
                found = False
                break
        if found:
            base = base[0:i] + base[i+len(remove):len(base)]
            i += len(remove)
        else:
            i += 1
    return base



print(without_string("Hello there", "llo")) # "He there"
print(without_string("Hello there", "e")) # "Hllo thr"
print(without_string("Hello there", "x")) # "Hello there"