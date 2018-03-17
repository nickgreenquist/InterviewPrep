from random import randint

def random_set(s, i, m, shuffled):
    if shuffled == m:
        return s
    
    random_set(s, i - 1, m, shuffled + 1)

    k = randint(0, i)
    tmp = s[k]
    s[k] = s[i]
    s[i] = tmp

    return s


s = [1,2,3,4,5,6,7,8,9,10]

m = 5
random_set(s, len(s) - 1, m, 0)
s = s[len(s) - m: len(s)]
print(s)