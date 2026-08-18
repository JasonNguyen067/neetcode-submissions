class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = float("inf")


    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.current_min:
            self.current_min = val

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.current_min = min(self.stack)
        else:
            self.current_min = float("inf")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min
