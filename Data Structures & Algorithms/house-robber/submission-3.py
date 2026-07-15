class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def loop(n):
            if n >= len(nums):
                return 0
            max_amount = max(nums[n] + loop(n + 2), loop(n + 1))
            return max_amount
        
        return loop(0)