class HeapNode():

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None

class MinHeap():

    def __init__(self):
        self.heap = []
    
    def _parent(self, i):
        return (i-1) // 2

    def _left(self, i):
        return (i*2) + 1

    def _right(self, i):
        return (i*2) + 2
    
    def _has_left(self, i):
        return self._left(i) < len(self.heap)
    
    def _has_right(self, i):
        return self._right(i) < len(self.heap)
    
    def _swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp
    
    def _upheap(self, i):
        """
        Bubble up value until not smaller than parent or hits root
        """
        while i > 0:
            p = self._parent(i)
            if self.heap[i] > self.heap[p]:
                break
            self._swap(i, p)
            i = p
    
    def _downheap(self, i):
        """
        Bubble down the value until smaller than both children or has no left child
        """
        while self._has_left(i):
            left_index = self._left(i)
            small_child_index = left_index
            if self._has_right(i):
                right_index = self._right(i)
                if self.heap[left_index] > self.heap[right_index]:
                    small_child_index = right_index
            if self.heap[small_child_index] > self.heap[i]:
                break
            self._swap(i, small_child_index)
            i = small_child_index

    def get_min(self):
        if len(self.heap) <= 0:
            return None
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)

        # bubble up the new item into it's correct place
        self._upheap(len(self.heap) - 1)

    def remove_min(self):
        if len(self.heap) <= 0:
            return None
        min_value = self.heap[0]

        # put the min item at the end
        self._swap(0, len(self.heap) - 1)

        # delete the last index
        del self.heap[-1]

        # fix the new root
        self._downheap(0)

        return min_value


if __name__ == "__main__":
    mh = MinHeap()

    # Test inserting things and seeing what the min is
    import random
    for i in range(100):
       mh.insert(random.randint(1,1000))

    while mh.get_min() is not None:
        print(mh.remove_min())
