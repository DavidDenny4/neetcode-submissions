class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        if n <= 2:
            return n
        return climbStairs(n - 2) + climbStairs(n - 1)