# Implement an automatically resizing vector.

class Vector:
    def __init__(self, capacity):
        self._array = [None for i in range(capacity)]
        self._size = 0
    def resize(self, new_capacity):
        if new_capacity > len(self._array):
            for i in range(len(self._array)):
                self._array.append(None)
        else:
            for i in range(len(self._array) // 2):
                self._array.pop()
    def size(self):
        return self._size
    def capacity(self):
        return len(self._array)
    def is_empty(self):
        return self._size < 1
    def at(self, i):
        if i >= len(self._array):
            return None
        return self._array[i]
    def push(self, item):
        if self._size >= len(self._array):
            self.resize((len(self._array) * 2))
        self._array[self._size] = item
        self._size += 1
    def insert(self, i, item):
        if i >= len(self._array):
            return None
        if i > self._size:
            self._size = i
        for j in range(i, len(self._array)):
            temp = self._array[j]
            self._array[j] = item
            item = temp
        if item is not None:
            self.push(item)
        else:
            self._size += 1
    def prepend(self, item):
        self.insert(0, item)
    def pop(self):
        self._size -= 1
        if self._size < 0:
            return None
        if self._size <= len(self._array) // 4:
            self.resize(len(self._array) // 2)
        ret = self._array[self._size]
        self._array[self._size] = None
        return ret
    def delete(self, i):
        if i < 0:
            return None
        for j in range(i, len(self._array) - 1):
            self._array[j] = self._array[j + 1]
        self._array[len(self._array) - 1] = None
        self._size -= 1
    def remove(self, item):
        i = 0
        while i < self._size:
            if self._array[i] == item:
                self.delete(i)
                i -= 1
            i += 1
    def find(self, item):
        for i in range(self._size):
            if self._array[i] == item:
                return i
        return -1



    
# TESTING
vec = Vector(4)
for i in range(4):
    vec.push(i)
print(vec._array)
vec.prepend(100)
vec.prepend(200)
vec.prepend(200)
vec.prepend(100)
print(vec._array)
vec.remove(100)
print(vec._array)
vec.remove(200)
print(vec._size)
print(vec._array)
vec.pop()
print(vec._array)
vec.pop()
print(vec._array)
print(vec._size)
vec.insert(3, 100)
print(vec._array)
vec.insert(3, 200)
print(vec._array)
