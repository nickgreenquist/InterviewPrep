import random

# Average case O(n) algorithm to the find the kth smallest element in list S
def quick_select(S, k):
    n = len(S)
    if n == 1:
        return S, S[0]

    # pick random pivot element
    i = random.randint(0, n-1)
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
        L, m = self.quick_select(L, k)
        return L + E + G, m
    elif k <= len(L) + len(E):
        return L + E + G, x
    else:
        G, m = self.quick_select(G, k - len(L) - len(E))
        return L + E + G, m
    
def wiggleSort(nums):
    n = len(nums)
    m = (n + 1) // 2
    A, median = quick_select(nums, m)
    L = []
    G = []
    E = []
    for num in A:
        if num == median:
            E.append(num)
        if num < median:
            L.append(num)
        if num > median:
            G.append(num)
    
    # elements larger than the 'median' are put into the first odd slots
    odds = 1
    j = 0
    while odds < n and j < len(G):
        nums[odds] = G[j]
        odds += 2
        j += 1
    
    # elements smaller than the 'median' are put into the last even slots
    evens = n - 1
    if evens % 2 != 0:
        evens -= 1
    j = 0
    while evens >= 0 and j < len(L):
        nums[evens] = L[j]
        evens -= 2
        j += 1
    
    # elements equal to median are put in remaining slots
    j = 0
    while odds < n:
        nums[odds] = E[j]
        odds += 2
        j += 1
    while evens >= 0:
        nums[evens] = E[j]
        evens -= 2
        j += 1


# Input:  [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]

nums = [1,5,1,1,6,4]
wiggleSort(nums)
print(nums)