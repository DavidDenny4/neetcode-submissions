class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = 0
        prev_sum = 0
        for R in range(2 * len(nums) - 1):
            prev_sum = max(prev_sum, 0)
            prev_sum += nums[R % len(nums)]
            max_sum = max(max_sum, prev_sum)
        return max_sum