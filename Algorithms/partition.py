# partitions elements around last element in arr
def partition(arr):
    L = 0
    H = len(arr) - 1

    ptr = 0
    x = arr[H]
    for i in range(0, H):
        if arr[i] <= x:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    
    arr[ptr], arr[H] = arr[H], arr[ptr]
    return arr

arr = [2, 7, 1, 0, 4, 3]
print(partition(arr))