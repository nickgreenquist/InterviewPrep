def most_frequent(arr):
    mf_element = None
    mf_element_count = -1
    count = {}
    for n in arr:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
        if count[n] > mf_element_count:
            mf_element_count = count[n]
            mf_element = n
    return mf_element

arr = [1,3,1,3,2,1]
print(most_frequent(arr))