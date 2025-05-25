def pivotArray(nums, pivot):
    """
    :type nums: List[int]
    :type pivot: int
    :rtype: List[int]
    """
    smaller = []
    larger = []
    equal = []

    for num in nums:
        if num == pivot:
            equal.append(num)
        elif num < pivot:
            smaller.append(num)
        else:
            larger.append(num)
    
    return smaller + equal + larger

nums = [9,12,5,10,14,3,10]
pivot = 10

expected = [9,5,3,10,10,12,14]
output = pivotArray(nums, pivot)
print(output)
print(expected == output)