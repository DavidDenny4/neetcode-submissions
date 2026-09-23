class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def loop(n):
            if n >= len(nums):
                return 0
            if n in cache:
                return cache[n]
            cache[n] = max(nums[n] + loop(n + 2), loop(n + 1))
            return cache[n]
        
        return loop(0)