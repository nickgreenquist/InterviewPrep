def freq(book, word):
    count = 0
    for w in book:
        if w == word:
            count += 1
    return count

def map(book):
    words = {}
    for w in book:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1


book = "the wind was windy and the beach"
book = book.split(" ")

ans = freq(book, "the")

print(ans)