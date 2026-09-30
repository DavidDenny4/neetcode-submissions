class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = 0
        prev_sum = 0
        for R in range(2 * len(nums) - 1):
            print(prev_sum)
            prev_sum = max(prev_sum, 0)
            prev_sum += nums[R % len(nums)]
            print(f"added {nums[R % len(nums)]} prev sum now {prev_sum}")
            max_sum = max(max_sum, prev_sum)
        return max_sum