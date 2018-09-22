import heapq

def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
    while k > 0:
        val = -heapq.heappop(heap)
        k -= 1
    return val

'''
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''
print(findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))