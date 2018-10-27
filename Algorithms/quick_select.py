from random import randint

# Average case O(n) algorithm to the find the kth smallest element in list S
def quick_select(S, k):
    n = len(S)
    if n == 1:
        return S[0]
    
    # pick random pivot element
    i = randint(0, n-1)
    x = S[i]

    L = [] # elements in S less than x
    E = [] # elements in S equal to x
    G = [] # elements in S greater than x

    for e in S:
        if e < x:
            L.append(e)
        elif e == x:
            E.append(e)
        else:
            G.append(e)
    
    if k <= len(L):
        return quick_select(L, k)
    elif k <= len(L) + len(E):
        return x
    else:
        return quick_select(G, k - len(L) - len(E))

S = [randint(0,100) for i in range(25)]

k = len(S) // 2
kth_smallest = quick_select(S, k)
print("Unsorted S: {}".format(S))
print("{}th_smallest element: {}".format(k, kth_smallest))
print("Sorted to confirm quick_select worked: {}".format(sorted(S)))

