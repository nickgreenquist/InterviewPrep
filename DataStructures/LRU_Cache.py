class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity):
        self.head = None
        self.tail = None
        
        self.capacity = capacity
        
        # maps key to Node object in memory
        self.map = {}
        
    def move_to_head(self, node):
        # if already head, nothing to move
        if self.head == node:
            return
        
        # if tail, point tail to tail.prev
        if self.tail == node:
            self.tail = self.tail.prev
                
        # remove node from DLL path
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        # make node new head
        self.head.prev = node
        node.next = self.head
        self.head = node

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.move_to_head(node)         
            return node.value
        
        return -1

    def put(self, key, value):      
        # Case: empty cache
        if self.head is None and self.tail is None:
            node = Node(key, value)
            self.head = node
            self.tail = node
            self.map[key] = node
        else:
            node = None
            if key in self.map:
                node = self.map[key]
                node.value = value
            else:
                node = Node(key, value)
                
            self.move_to_head(node)
            self.map[key] = node
            
            if len(self.map.keys()) > self.capacity:
                del self.map[self.tail.key]
                
                new_tail = self.tail.prev
                if new_tail:
                    new_tail.next = None
                    
                self.tail = new_tail


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(2))
lru.put(2, 3)
print(lru.get(2))

# key 1 should be evicted
lru.put(3, 3)
print(lru.get(1))