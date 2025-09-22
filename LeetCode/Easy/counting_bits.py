def countBitsNonOptimal(n):
    """
    :type n: int
    :rtype: List[int]
    """
    def numberOfOnesSet(x):
        count = 0
        while x:
            x = x & (x-1)
            count += 1
        return count

    res = []
    for i in range(n+1):
        res.append(numberOfOnesSet(i))
    return res

def countingBits(n):
    dp = [0] * (n+1)

    offset = 1 # highest power of 2
    for i in range(1, n+1):
        if offset * 2 == i:
            offset *= 2
        dp[i] = dp[i-offset] + 1
    
    return dp

'''
0 - 0000
1 - 0001
2 - 0010
3 - 0011
4 - 0100
5 - 0101
you can see if we shift 5 to the right by 1, and it becomes 2,
and 5 & 1 is 1, so the number of 1's in 5, is actually the number of 1's in 2 plus 1,
because 5&1 == 1.

similarly, if we shift 4 to the right by 1, which becomes 2 as well,
and 4&1 is 0, so number of 1's in 4, is the the number of 1's in 2 plus 0,
because 4&1 == 0.

i=3
dp[3] = dp[3 >> 1] + (3 % 1)
dp[3] = dp[0011 >> 1] + (0011 % 1)
dp[3] = dp[0001] + (1)
dp[3] = dp[1] + (1)
'''
def countingBitsLeftShift(n):
    dp = [0] * (n+1)

    for i in range(1, n+1):
        dp[i] = dp[i>>1] + (i & 1)
    
    return dp


'''
Input: n = 5
Output: [0,1,1,2,1,2]
'''

print(countBitsNonOptimal(5))
print(countingBits(5))
print(countingBitsLeftShift(5))