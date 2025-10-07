def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    # 1. while loop
    # 2. check if need to carry over anything (use &)
    # 3. xor
    # 4. shift left

    carry = 0
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

def getSumNeetcode(a, b):
    # a ^ b
    # (a & b) << 1
    # the above two steps are equivalent to addition

    temp = 0
    while b:
        temp = a ^ b
        b = (a & b) << 1
        a = temp
    return a

'''
// Java
class Solution {
    public int getSum(int a, int b) {
        int temp = 0;
        while (b != 0) {
            temp = a ^ b;
            b = (a & b) << 1;
            a = temp;
        }
        return a;
    }
}
'''

print(getSum(5, 90))
print(getSumNeetcode(5, 90))