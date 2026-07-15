class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        if n <= 2:
            return n
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)