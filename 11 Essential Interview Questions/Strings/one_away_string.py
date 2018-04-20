def one_edit(a, b):
    # 1. Change character
    # 2. Delete
    # 3. Add
    if a == b:
        return True
    i = 0
    j = 0
    edits = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            edits += 1
            if len(a) == len(b):
                i += 1
                j += 1
            elif len(a) > len(b):
                i += 1
            else:
                j += 1
    # add any leftoever characters
    edits += (len(a) - i) + (len(b) - j)
    return edits < 2
        

print(one_edit('abcde','abfde'))
print(one_edit('xyz','xyaz'))
print(one_edit('abcde','abde'))
print(one_edit('abcdef','abcd'))