def levenshtein_distance(a, b, a_head, b_head, lookup):
    if lookup[a_head][b_head] >= 0:
        return lookup[a_head][b_head]

    if a_head >= len(a):
        lookup[a_head][b_head] = len(b) - b_head
        return lookup[a_head][b_head]
    if b_head >= len(b):
        lookup[a_head][b_head] = len(a) - a_head
        return lookup[a_head][b_head]
    if a[a_head] == b[b_head]:
        lookup[a_head][b_head] = levenshtein_distance(a, b, a_head + 1, b_head + 1, lookup)
        return lookup[a_head][b_head]
    
    insertion = levenshtein_distance(a, b, a_head + 1, b_head, lookup) + 1
    deletion = levenshtein_distance(a, b, a_head, b_head + 1, lookup) + 1
    substitution = levenshtein_distance(a, b, a_head + 1, b_head + 1, lookup) + 2
    lookup[a_head][b_head] = min(insertion, deletion, substitution)
    return lookup[a_head][b_head]

a = 'intention'
b = 'execution'

N = len(a) + 1
M = len(b) + 1

lookup = [[-1]*(M) for i in range(N)]

dist = levenshtein_distance(a, b, 0, 0, lookup)
print(dist)