class Solution:
    def climbStairs(self, n: int) -> int:
        pre, curr = 0, 1
        for i in range(n):
            pre, curr = curr, pre + curr
        return curr
