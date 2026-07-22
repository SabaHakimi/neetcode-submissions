class MinStack:

    def __init__(self):
        # stores tuples, formatted as:
        # (val, current_minimum)
        self.stack = []
        

    def push(self, val: int) -> None:
        min = None
        if not self.stack or val < self.getMin():
            min = val
        else:
            min = self.getMin()

        self.stack.append((val, min))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
