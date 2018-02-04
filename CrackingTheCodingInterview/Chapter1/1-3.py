def urlify(s, l):
    s = s.split()
    l = len(s)
    newString = ""
    for i in range(l):
        if i != l - 1:
            newString += (s[i] + "%20")
        else:
            newString += s[i]
    return newString.strip()

s = "Mr John Smith  "
print (urlify(s, len(s)))