class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.push(val)
        curr_min = self.min_stack[-1]
        if val < curr_min:
            self.min_stack.push(val)
        else:
            self.min_stack.push(curr_min)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
