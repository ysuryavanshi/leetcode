class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.size = 0
        self.stack = []
        
    def push(self, x: int) -> None:
        if self.size < self.max_size:
            self.stack.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        k = k if k <= self.size else self.size
        for i in range(k):
            self.stack[i] += val        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)