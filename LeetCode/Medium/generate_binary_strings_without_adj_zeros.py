def validStrings(n):
    """
    :type n: int
    :rtype: List[str]
    """
    output = []
    def build(current, n):
        if len(current) == n:
            return output.append(current)

        if current[-1] == '1':
            build(current + '0', n)
        build(current + '1', n)
            
    build('0', n)
    build('1', n)
    return output

'''
Input: n = 3
Output: ["010","011","101","110","111"]
'''

print(validStrings(3))