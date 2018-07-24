def get_longest_word(words):
    # array = sorted(words)
    bag = {}
    for a in words:
        bag[a] = True

    print(bag)

    for a in words:
        if can_build_word(a, True, bag):
            return a

def can_build_word(s, orig, bag):
    if s in bag and not orig:
        return bag[s]
    for i in range(1, len(s)):
        left = s[0:i]
        right = s[i:]
        if left in bag and bag[left] and can_build_word(right, False, bag):
            return True
    bag[s] = False
    return False
    
words = ['l;kjasdlfkjas;lkd', 'looksee', 'look', 'see', 'banana']
print(get_longest_word(words))
