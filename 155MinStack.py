class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []  

    def push(self, x: int) -> None:
        cur_min = self.getMin()
        if cur_min == None or x < cur_min: cur_min = x
        self.s.append((x, cur_min))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        if not self.s: return None
        return self.s[-1][0]

    def getMin(self) -> int:
        if not self.s: return None
        return self.s[-1][1]
