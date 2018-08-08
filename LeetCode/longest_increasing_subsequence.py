def LIS(arr):
    n = len(arr)

    lookup = [1]*n #lookup[i] = longest LIS ending with this value at arr[i]

    for i in range(1, n):
        for j in range(0, i):
            # if this number if bigger than one before and the
            # lookup of the one before is bigger than the best
            # i can make ending at this number
            if arr[i] > arr[j] and lookup[i] < lookup[j] + 1:
                lookup[i] = lookup[j] + 1
    return max(lookup)


arr = [300, 120, 400, 200, 10, 300, 1, 2, 3, 4, 5]
print(LIS(arr))