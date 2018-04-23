'''
Return an array that contains the sorted values from the input array with duplicates removed.
'''

def sort(arr):
    arr = sorted(arr)
    last = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] == last:
            del arr[i]
            i -= 1
        last = arr[i]
        i += 1
    return arr

print(sort([5,6,1,7,4,4,4,4,7,8,3,3,2]))
print(sort([1,1]))
