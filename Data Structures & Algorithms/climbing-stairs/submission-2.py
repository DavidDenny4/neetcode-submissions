class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        cache = {}
        if n <= 2:
            return n
        if n in cache:
            return cache[n]
        cache[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        return cache[n]