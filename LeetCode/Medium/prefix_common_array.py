def findThePrefixCommonArray(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    seen_A = set()
    seen_B = set()
    output = []
    total = 0
    for i in range(len(A)):
        a = A[i]
        seen_A.add(a)
        b = B[i]
        seen_B.add(b)
        if a == b:
            total += 1
            output.append(total)
        else:
            if a in seen_B:
                total += 1
            if b in seen_A:
                total += 1
            output.append(total)
    return output


'''
Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
'''
A = [1,3,2,4]
B = [3,1,2,4]
expected = [0,2,3,4]
print(findThePrefixCommonArray(A, B) == expected)