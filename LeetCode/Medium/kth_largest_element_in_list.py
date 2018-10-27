from random import randint

def findKthLargest(nums, k):
    def quick_select(nums, k):
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        
        p = randint(0, n-1)
        x = nums[p]
        
        L = []
        E = []
        G = []
        for num in nums:
            if num < x:
                L.append(num)
            elif num == x:
                E.append(num)
            else:
                G.append(num)
        
        if k <= len(G):
            return quick_select(G, k)
        elif k <= len(G) + len(E):
            return x
        else:
            return quick_select(L, k - len(G) - len(E))
    
    return quick_select(nums, k)
            
        

'''
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''
print(findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))