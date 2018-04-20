def most_common(A, B):
    i = 0
    j = 0
    common = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            common.append(A[i])
            i += 1
            j += 1
        else:
            if A[i] > B[j]:
                j += 1
            else:
                i += 1
    return common
        

A = [1,3,4,6,7,9]
B = [1,2,4,5,9,10]

print(most_common(A, B))