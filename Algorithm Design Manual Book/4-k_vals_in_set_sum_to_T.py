def TwoSum(A, T):
    B = {}
    for i in range(0, len(A)):
        val = T - A[i]
        if val in B:
            B[val].add(i)
        else:
            B[val] = set([i])
    
    for i in range(0, len(A)):
        val = A[i]
        if val in B:
            # check if set contains more than just your own index
            # (to prevent one number being added to itself equaling T)
            indices_that_make_val = B[val]
            if len(indices_that_make_val) == 1:
                index_seen = list(indices_that_make_val)[0]
                return index_seen != i
            else:
                return True
    return False

def CheckSumK(A, k, T):
    print("k: " + str(k) + ", A: " + str(A) + ", T: " + str(T))
    if k == 2:
        hasTwoSum = TwoSum(A, T)
        print("hasTwoSum: " + str(hasTwoSum))
        return hasTwoSum
    n = len(A)
    B = []
    for i in range(n-1):
        k = 0
        for j in range(n-1):
            if i != j:
                B.append(A[j])
                k = k + 1
        
        # If A[i] is in the k integers that sum to T, 
        # then there must bc k-1 ints that sum to T - B[i]
        if CheckSumK(B, k - 1, T - B[i]):
            return True
    return False

A = [1,2,3,4,5]
T = 11

print(CheckSumK(A, 3, T))