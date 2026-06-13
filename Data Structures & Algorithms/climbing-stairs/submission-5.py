class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        cache = {}

        def stairs(n):
            if n <= 2:
                return n
            if n in cache:
                return cache[n]
            cache[n] = stairs(n - 2) + stairs(n - 1)
            return cache[n]
        
        return stairs(n)