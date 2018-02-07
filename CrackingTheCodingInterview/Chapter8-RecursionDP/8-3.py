def MagicIndex(array, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    midval = array[mid]
    if mid == midval:
        return mid

    leftIndex = min(mid - 1, midval)
    left = MagicIndex(array, start, leftIndex)
    if left >= 0:
        return left

    rightIndex = max(mid + 1, midval)
    right = MagicIndex(array, rightIndex, end)
    if right >= 0:
        return right
    
    return -1


#array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
array = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
magic = MagicIndex(array, 0, len(array))
print(magic)