def tripleIsSorted(A, m):
    if m == len(A) - 1:
        return A[m-1] + 1 == A[m]
    elif m == 0:
        return A[m] + 1 == A[m+1]
    else:
        return (A[m-1] + 1 == A[m]) and (A[m] + 1 == A[m + 1])

def findMissing(A, L, H):
    if L >= H:
        if not tripleIsSorted(A, L):
            return L
        else:
            return None
    if A[0] != 1:
        return 1
    if A[-1] != len(A) + 1:
        return len(A) + 1
    
    mid = L + ((H - L) // 2)

    # missing number is to the right
    if mid + 1 == A[mid]:
        return findMissing(A, mid, H)
    elif mid + 1 > A[mid]:
        return findMissing(A, L, mid)
    else:
        # check if A[mid-1], A[mid], and A[mid+1] are in order
        if not tripleIsSorted(A, mid):
            return mid + 1
        else:
            return findMissing(A, L, mid)

# A = [1...10] with 8 missing
A = [1,2,3,4,5,6,7,9,10]
print(findMissing(A, 0, len(A)))

# A = [1...11] with 10 missing
A = [1,2,3,4,5,6,7,8,9,10,11]
print(findMissing(A, 0, len(A)))

