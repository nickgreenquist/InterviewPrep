from random import randint

def max_bounded(array, left, right):
    m = float('-inf')
    for i in range(left, right + 1):
        m = max(m, array[i])
    return m

def rank_large(array, left, right, rank):
    pivot = array[randint(left, right)]
    leftEnd = partition(array, left, right, pivot)
    leftSize = leftEnd - left + 1
    if rank == leftSize - 1:
        return max_bounded(array, left, leftEnd)
    elif rank < leftSize:
        return rank_large(array, left, leftEnd, rank)
    else:
        return rank_large(array, leftEnd + 1, right, rank - leftSize)

def partition(array, left, right, pivot):
    while left <= right:
        if array[left] > pivot:
            tmp = array[left]
            array[left] = array[right]
            array[right] = tmp
            right -= 1
        elif array[right] <= pivot:
            tmp = array[left]
            array[left] = array[right]
            array[right] = tmp
            left += 1
        else:
            left += 1
            right -= 1
    return left - 1


def rank_small(array, rank):
    return rank_large(array, 0, len(array) - 1, rank)

def smallestK(array, k):
    if k <= 0 or k > len(array):
        return None
    threshold = rank_small(array, k - 1)
    smallest = [0 for i in range(k)]
    count = 0
    for a in array:
        if a <= threshold:
            smallest[count] = a
            count += 1
    return smallest

test = [i for i in range(100)]
smallest = smallestK(test, 10)
print(smallest)