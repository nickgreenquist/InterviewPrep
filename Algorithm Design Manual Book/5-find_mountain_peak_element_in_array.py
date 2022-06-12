def bs(arr, L, H):
    if L >= H:
        return L
    
    m = L + ((H - L) // 2)
    if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
        return m
    elif arr[m] > arr[m+1]:
        return bs(arr, L, m)
    else:
        return bs(arr, m, H)
    
def peakIndexInMountainArray(arr):
    return bs(arr, 0, len(arr))

'''
Input: arr = [0,10,5,2]
Output: 1
'''
arr = [0,10,5,2]
print(peakIndexInMountainArray(arr))