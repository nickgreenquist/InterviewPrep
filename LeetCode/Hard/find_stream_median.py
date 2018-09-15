from heapq import *

class MinHeap():
    def __init__(self):
        self.heap = []
        
    def push(self, num):
        heappush(self.heap, num)
    
    def pop(self):
        return heappop(self.heap)
    
class MaxHeap():
    def __init__(self):
        self.heap = []
        
    def push(self, num):
        heappush(self.heap, -1 * num)
    
    def pop(self):
        return -1 * heappop(self.heap)

class MedianFinder(object):
    def __init__(self):
        self.left = MaxHeap()
        self.right = MinHeap()

    def addNum(self, num):
        
        # add the number to the right heap
        self.right.push(num)
        
        # get the smallest number from the right heap (middle value)
        smallest_from_right = self.right.pop()
        
        # add to the right heap
        self.left.push(smallest_from_right)
        
        if len(self.right.heap) < len(self.left.heap):
            largest_from_left = self.left.pop()
            
            self.right.push(largest_from_left)

    def findMedian(self):
        if len(self.right.heap) > len(self.left.heap):
            return float(self.right.heap[0])
        
        # median is the average of the middle two values
        return (self.right.heap[0] - self.left.heap[0]) / 2.0
        
'''
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
'''

mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())
