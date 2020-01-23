class MyStack:

    def __init__(self):
        self.stack = collections.deque()
    
    def empty(self):
        return not len(self.stack)

    def push(self, x: int) -> None:
        q = self.stack
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not len(self.stack)
