
'''
Find the shortest lenth subset of an array that needs to be
sorted such that the entire array is sorted
'''

def sub_sort(A):
    max_seen = float('-inf')
    n = 0
    for i in range(len(A)):
        num = A[i]
        max_seen = max(num, max_seen)
        if num < max_seen:
            n = i

    min_seen = float('inf')
    m = 0
    for i in range(len(A) - 1, 0, -1):
        num = A[i]
        min_seen = min(num, min_seen)
        if num > min_seen:
            m = i

    return n, m

A = [1, 2, 4, 7, 10, 11, 8, 12, 6, 7, 16, 18, 19]
print(sub_sort(A))