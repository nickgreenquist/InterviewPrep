def reverseBitsNeetcode(n):
    """
    :type n: int
    :rtype: int
    """
    res = 0
    for i in range(32):
        # get ith bit of n
        bit = (n >> i) & 1 # 1 or 0 in ith index of n
        res = res | (bit << (31 - i))
    return res

def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):
        # shift left to make room for next bit
        res = res << 1

        # add the rightmost bit of n
        res = res | (n & 1)

        # shift the n to right to get the next bit
        n = n >> 1
    return res

'''
Input: n = 43261596
Output: 964176192
'''
print(reverseBits(43261596))