class Node():
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.cap = capacity
        self.cache = {}
        
        # stores node mem address with cache key as key
        self.nodes = {}

    def get(self, key):
        if key not in self.cache:
            return -1
        
        val = self.cache[key]     
        node = self.nodes[key]
        
        if node != self.head: 
            if node == self.tail:
                self.tail = self.tail.prev
            
            # remove from current spot
            prev = node.prev
            succ = node.next

            if prev:
                prev.next = succ
            if succ:
                succ.prev = prev

            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node
            
        return val

    def put(self, key, value):
        # update key's value and move to front of list   
        if key in self.cache:
            self.cache[key] = value
            return self.get(key)
        
        # evict key from end of list
        if self.cap <= 0:
            evict = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            
            self.nodes.pop(evict.key)
            self.cache.pop(evict.key)
            
            self.cap += 1
        
        # add new node to front of list
        add = Node(key)
        if self.head:
            self.head.prev = add
            add.next = self.head   
        self.head = add
        
        self.cache[key] = value
        self.nodes[key] = add
        
        self.cap -= 1
        
        if not self.tail:
            self.tail = add
        
        return value

cache = LRUCache(2)        # capacity = 2
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))        # returns 1
cache.put(3, 3)            # evicts key 2
print(cache.get(2))        # returns -1 (not found)
cache.put(4, 4)            # evicts key 1
print(cache.get(1))        # returns -1 (not found)
print(cache.get(3))        # returns 3
print(cache.get(4))        # returns 4