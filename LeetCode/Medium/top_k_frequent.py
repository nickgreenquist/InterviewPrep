def topKFrequent(nums, k):
    counts = {}
    for n in nums:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
            
    buckets = {}
    for i in range(1, len(nums) + 1):
        buckets[i] = []
    
    for key,val in counts.items():
        buckets[val].append(key)
    
    top_k = []
    to_add = k
    for i in range(len(nums), 0, -1):
        top_k += buckets[i]
        to_add -= len(buckets[i])
        if to_add < 1:
            break
    return top_k[:k]
'''
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''
print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))