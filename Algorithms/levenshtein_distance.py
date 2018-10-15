def levenshtein_distance(s1, s2):
    N = len(s1) + 1
    M = len(s2) + 1

    lookup = [[0]*(M) for i in range(N)]

    # left and bottom border is always i edits
    for i in range(N):
        lookup[i][0] = i
    for i in range(M):
        lookup[0][i] = i

    for i in range(1, N):
        for j in range(1, M):
            subsitution = 0 if s1[i-1] == s2[j-1] else 2
            lookup[i][j] = min(
                lookup[i-1][j] + 1, # deletion
                lookup[i][j-1] + 1, # insertion
                lookup[i-1][j-1] + subsitution
            )

    return lookup[N-1][M-1], lookup

def backtrace(lookup, s1, s2):
    N = len(lookup)
    M = len(lookup[0])

    i = N-1
    j = M-1
    solution = ''
    while i >= 0 and j >= 0:
        best_move = min(lookup[i-1][j], lookup[i-1][j-1], lookup[i][j-1])
        if best_move == lookup[i-1][j]:
            if i-1 >= 0:
                solution = 'deletion {} at {} --> '.format(s1[i-1], i-1) + solution
            i -= 1
        elif best_move == lookup[i-1][j-1]:
            if i-1 >= 0 and j-1 >= 0 and lookup[i-1][j-1] != lookup[i][j]:
                solution = 'subsitution {} for {} at {} --> '.format(s1[i-1], s2[j-1], i-1) + solution
            i -= 1
            j -= 1
        else:
            if j-1 >= 0:
                solution = 'insertion {} at {} --> '.format(s2[j-1], j-1) + solution
            j -= 1
    return solution
    



s1 = 'intention'
s2 = 'execution'
dist, lookup = levenshtein_distance(s1, s2)
print(dist)

solution = backtrace(lookup, s1, s2)
print(solution)
