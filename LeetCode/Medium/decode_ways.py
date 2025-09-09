def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    def numWays(s, n, i):
        if i >= n:
            return 1

        if i in lookup:
            return lookup[i]

        ways = 0

        # use two chars
        if i < n-1 and ((s[i] == '1') or (s[i] == '2' and s[i+1] >= '0' and s[i+1] <= '6')):
            ways += numWays(s, n, i + 2)

        # use only this char
        if int(s[i]) != 0:
            ways += numWays(s, n, i + 1)

        lookup[i] = ways
        return lookup[i]
    
    if s[0] == '0':
        return 0
    
    lookup = {}
    ways = numWays(s, len(s), 0)
    return ways

s = "2611055971756562"
print(numDecodings(s) == 4)