def find_two(arr, start, product):
    d = {}
    for i in range(start, len(arr)):
        n = arr[i]
        goal = product / n
        if goal in d:
            return (n, arr[d[goal]])
        d[n] = i
    return None

def find_three(arr, product):
    for i in range(0, len(arr)):
        n = arr[i]
        goal = product / n
        pair = find_two(arr, i + 1, goal)
        if pair:
            return (n, pair[0], pair[1])
    return None


arr = [2,4,1,6,5,40,-1]
print(find_three(arr, 120))