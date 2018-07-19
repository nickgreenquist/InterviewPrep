
def min_word_distance_in_doc(doc, word1, word2):
    doc = doc.split(' ')
    a1 = []
    a2 = []
    for i in range(len(doc)):
        word = doc[i]
        if word == word1:
            a1.append(i)
        if word == word2:
            a2.append(i)

    i = 0
    j = 0
    m = float('inf')
    while i < len(a1) and j < len(a2):
        m = min(m, abs(a1[i] - a2[j]))
        if a1[i] < a2[j]:
            i += 1
        else:
            j += 1
    return m



doc = "four blah blah blah one two three one blah four blah blah blah blah four"
print(min_word_distance_in_doc(doc, 'one', 'four'))