def convertDateToBinary(date):
    """
    :type date: str
    :rtype: str
    """
    output = '-'.join([format(int(x), 'b') for x in date.split('-')])

    return output

'''
Input: date = "2080-02-29"
Output: "100000100000-10-11101"
'''

date = "2080-02-29"
expected = "100000100000-10-11101"
print(convertDateToBinary(date) == expected)