'''
Write a function that replaces the words in `raw` with the words in `code_words` 
such that the first occurrence of each word in `raw` is assigned the first unassigned word in `code_words`.
'''

def encoder(raw, codes):
    next_raw = 0
    d = {}
    for i in range(len(raw)):
        if raw[i] in d:
            raw[i] = d[raw[i]]
        else:
            d[raw[i]] = codes[next_raw]
            next_raw += 1

            raw[i] = d[raw[i]]
    return raw

print(encoder(["a"], ["1", "2", "3", "4"])) # ["1"]
print(encoder(["a", "b"], ["1", "2", "3", "4"])) # ["1", "2"]
print(encoder(["a", "b", "a"], ["1", "2", "3", "4"])) # ["1", "2", "1"]