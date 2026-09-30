class Solution:
    def rob(self, nums: List[int]) -> int:

        def total(n):
            sum = 0
            while n >= 0:
                sum += nums[n]
                n -= 2
            return sum
        
        length = len(nums)
        if length == 1:
            return nums[0]
        return max(total(length - 1), total(length - 2))
