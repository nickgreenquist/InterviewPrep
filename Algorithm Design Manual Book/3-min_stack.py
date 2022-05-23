class MinStack:
    def __init__(self):
        self.main = []
        self.aux = []

    def push(self, val: int) -> None:
        self.main.append(val)
        if len(self.aux) == 0:
            self.aux.append(val)
        elif len(self.aux) > 0 and val <= self.aux[-1]:
            self.aux.append(val)

    def pop(self) -> None:
        val = self.main.pop()
        if val == self.aux[-1]:
            self.aux.pop()

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.aux[-1]

min_stack = MinStack()
min_stack.push(1)
min_stack.push(0)
min_stack.push(2)
min_stack.push(0)
print(min_stack.getMin())

min_stack.pop()
print(min_stack.getMin())

min_stack.pop()
min_stack.pop()
print(min_stack.getMin())