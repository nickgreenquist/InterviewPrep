class Queue:
    def __init__(self, s):
        self.array = [None for i in range(s)]
        self.front = 0
        self.back = 0
        self.size = s
    def print(self):
        print('Front: %s' % (self.front))
        print('Back: %s' % (self.back))
        if self.empty():
            return None
        elif self.singleton():
            print(self.array[self.front])
        else:
            i = self.front
            while i != self.back:
                print(self.array[i])
                i += 1
                if i >= self.size:
                    i = 0
            print(self.array[i])
            print()
    def empty(self):
        return self.front == self.back and self.array[self.front] is None
    def singleton(self):
        return self.front == self.back and self.array[self.front] is not None
    def full(self):
        if self.back == self.size - 1 and self.front == 0:
            return True
        else:
            return self.back + 1 == self.front
    def enqueue(self, value):
        if self.empty():
            self.array[self.front] = value
        elif self.full():
            print('FULL')
        else:
            self.back += 1
            if self.back >= self.size:
                self.back = 0
            self.array[self.back] = value
    def dequeue(self):
        if self.empty():
            print('EMPTY')
        elif self.singleton():
            tmp = self.array[self.front]
            self.array[self.front] = None
            return tmp
        else:
            tmp = self.array[self.front]
            self.array[self.front] = None
            self.front += 1
            if self.front >= self.size:
                self.front = 0
            return tmp
    

# Test calls
q = Queue(5)
for i in range(1, 6):
    q.enqueue(i)

q.print()

q.dequeue()
q.dequeue()
q.enqueue(6)

q.print()



