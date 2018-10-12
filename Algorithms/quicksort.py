def partition(arr, low, high):
    pivot = arr[high]

    j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    arr[j], arr[high] = arr[high], arr[j]
    return j

def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

arr = [2, 1, 7, 0, 4, 3]
quicksort(arr, 0, len(arr) - 1)
print(arr)