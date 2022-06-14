import random

def getK(A, AL, B, BL, k, n, m):
    if AL > n - 1:
        return B[BL + k - 1]
    if BL > m - 1:
        return A[AL + k - 1]
    
    if k == 1:
        return min(A[AL], B[BL])
    
    AM = 9999999
    BM = 9999999
    if AL + (k//2) - 1 < n:
        AM = A[AL + (k//2) - 1]
    if BL + (k//2) - 1 < m:
        BM = B[BL + (k//2) - 1]
    
    if AM < BM: # A right of AM, B left side
        return getK(A, AL + (k//2), B, BL, k - (k//2), n, m)
    else: # A left side, B right of BM
        return getK(A, AL, B, BL + (k//2), k - (k//2), n, m)
            
        
def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    if (n + m) % 2 == 0:
        L = (n + m + 1) // 2
        R = (n + m + 2) // 2
        med1 = getK(nums1, 0, nums2, 0, L, n, m)
        med2 = getK(nums1, 0, nums2, 0, R, n, m)
        return (med1 + med2) / 2.0
    else:
        return getK(nums1, 0, nums2, 0, (n+m + 1) // 2, n, m)

A = sorted([random.randint(0,100) for i in range(24)])
B = sorted([random.randint(0,100) for i in range(25)])

# O(log(n + m))
print(findMedianSortedArrays(A, B))

# O(m + n): merge two sorted arrays is trivial solution
print(sorted(A + B)[49 // 2])