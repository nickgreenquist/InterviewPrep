def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    x = nums[:n]
    y = nums[n:]
    out = []
    for i in range(n):
        out.append(x[i])
        out.append(y[i])

    return out

nums = [2,5,1,3,4,7]
expected = [2,3,5,4,1,7]

print(shuffle(nums, len(nums) // 2) == expected)