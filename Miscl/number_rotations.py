class NumberRotationSolution(object):
    def canRotate(self, N):
        while N > 0:
            digit = N % 10
            if digit == 3 or digit == 4 or digit == 7:
                return False
            N = N / 10
        return True
    def isValidRotation(self, N):
        while N > 0:
            digit = N % 10
            if digit == 2 or digit == 5 or digit == 6 or digit == 9:
                return True
            N = N / 10
        return False
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(1, N + 1):
            if self.canRotate(i) and self.isValidRotation(i):
                count += 1
        return count

'''
Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
'''
print(NumberRotationSolution().rotatedDigits(10))