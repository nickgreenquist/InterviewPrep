def find_majority(arr):
    cand = candidate(arr)

    count = 0
    for n in arr:
        if n == cand:
            count += 1
    if count >= len(arr) // 2:
        return cand
    else:
        return -1

def candidate(arr):
    maj = 0
    count = 0
    for num in arr:
        if count == 0:
            maj = num 
            count = 1
        elif num == maj:
            count += 1
        else:
            count -= 1
    return maj


arr = [1,2,5,9,5,9,5,5]
print(find_majority(arr))