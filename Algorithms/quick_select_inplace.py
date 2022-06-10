
from random import randint

def partition(arr, L, H):
    ptr = L
    x = arr[H]
    for i in range(L, H):
        if arr[i] <= x:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    
    arr[ptr], arr[H] = arr[H], arr[ptr]
    return ptr

# find kth smallest element in array
def qs(arr, k, L, H):
    if L > H:
        print("ERROR")
        return -1
    if L == H:
        return L
    
    p_idx = partition(arr, L, H)
    if p_idx == k:
        return p_idx
    elif k < p_idx:
        return qs(arr, k, L, p_idx - 1)
    else:
        return qs(arr, k, p_idx + 1, H)


S = [randint(0,100) for i in range(25)]
print("Unsorted S: {}".format(S))

k = len(S) // 2
kth_smallest_idx = qs(S, k, 0, len(S) - 1)
print("After quick_select S: {}".format(S))
print("{}th_smalled_idx: {}".format(k, kth_smallest_idx))
print("{}th_smallest element: {}".format(k, S[kth_smallest_idx]))
print("Sorted to confirm quick_select worked: {}".format(sorted(S)))
print("{}th_smalled_element from sorted S: {}".format(k, sorted(S)[k]))

print("Verify correctness in 100 random arrays: find median")
correct = 0
errors = 0
for i in range(100):
    S = [randint(0,100) for i in range(25)]
    k = len(S) // 2
    kth_smallest_idx = qs(S, k, 0, len(S) - 1)
    if S[kth_smallest_idx] != sorted(S)[k]:
        errors += 1
    else:
        correct += 1
print("CORRECTS: {}".format(correct))
print("ERROR: {}".format(errors))

print("Verify correctness in 100 random arrays: find second to last biggest element")
correct = 0
errors = 0
for i in range(100):
    S = [randint(0,100) for i in range(25)]
    k = len(S) - 2
    kth_smallest_idx = qs(S, k, 0, len(S) - 1)
    if S[kth_smallest_idx] != sorted(S)[k]:
        errors += 1
    else:
        correct += 1
print("CORRECTS: {}".format(correct))
print("ERROR: {}".format(errors))
