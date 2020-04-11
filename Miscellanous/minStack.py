class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.minS = []
        

    def push(self, x: int) -> None:
        n = len(self.items)
        if n == 0:
            self.minS.append(x)
        else:
            lastMin = self.minS[-1]
            if x <= lastMin:
                self.minS.append(x)
        self.items.append(x)

    def pop(self) -> None:
        return self.items.pop()

    def top(self) -> int:
        return self.items[len(self.items) - 1]

    def getMin(self) -> int:
        return self.minS[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()