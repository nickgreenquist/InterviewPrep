'''
Given a list of non negative integers, arrange them such that they form the largest number.
'''
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def largestNumber(nums):
    comp=lambda a,b:1 if a+b>b+a else -1 if a+b<b+a else 0
    
    nums = map(str,nums)
    nums = sorted(nums, key=cmp_to_key(comp), reverse=True)
    
    num = "".join(c for c in nums)
    if int(num) == 0:
        return '0'
    return num

'''
Example 1:
Input: [10,2]
Output: "210"
'''
print(largestNumber([10,2]))

'''
Example 2:
Input: [3,30,34,5,9]
Output: "9534330"
'''
print(largestNumber([3,30,34,5,9]))