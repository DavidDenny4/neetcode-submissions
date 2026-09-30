class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        cache = {}

        def stairs(n):
            if n <= 2:
                return n
            if n in self.cache:
                return self.cache[n]
            self.cache[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
            return self.cache[n]
        
        return stairs(n)