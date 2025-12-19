class MinStack:

    def __init__(self):
        self.stack = []
        self.min: int = 10**10
        self.min_lst = [10**10]
        
    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        if self.min == val:
            self.min_lst.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.min == popped:
            self.min_lst.pop()
            self.min = self.min_lst[-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()