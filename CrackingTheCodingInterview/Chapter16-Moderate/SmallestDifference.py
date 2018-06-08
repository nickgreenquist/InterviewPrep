def smallest_diff(A, B):
    A = sorted(A)
    B = sorted(B)
    i = j = 0
    smallest = float('inf')
    smallest_i = smallest_j = 0
    while i < len(A) and j < len(B):
        diff = abs(A[i] - B[j])
        if diff < smallest:
            smallest = diff
            smallest_i = i
            smallest_j = j
        if A[i] < B[i]:
            i += 1
        else:
            j += 1
    return (smallest, A[smallest_i], B[smallest_j])

A = [1,3,15,11,2]
B = [23,127,235,19,8]
print(smallest_diff(A, B))