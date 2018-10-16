def sort(arr):
    merge_sort(arr, 0, len(arr) - 1)

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    left_size = mid - low + 1
    right_size = high - mid
    left = [0]*left_size
    right = [0]*right_size

    # copy elements from range in arr to temp arrays
    for i in range(left_size):
        left[i] = arr[i + low]
    for i in range(right_size):
        right[i] = arr[i + mid + 1]
    
    # merge arrays correctly back into correct range in arr
    i = 0
    j = 0
    k = low
    while i < left_size and j < right_size:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # add leftovers if needed
    if i < left_size:
        while i < left_size:
            arr[k] = left[i]
            k += 1
            i += 1
    if j < right_size:
        while j < right_size:
            arr[k] = right[j]
            k += 1
            j += 1

from random import randint
arr = []
for i in range(25):
    arr.append(randint(1, 99))

sort(arr)
print(arr)