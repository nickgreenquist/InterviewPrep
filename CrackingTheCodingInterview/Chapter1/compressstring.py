def compress(s):
    newString = ""
    count = 1
    last = s[0]
    for i in range(1, len(s)):
        if last == s[i]:
            count += 1
        else:
            newString += (last + str(count))
            last = s[i]
            count = 1
    newString += (last + str(count))
    return newString

s = 'aabcccccaaag'
print(compress(s))