class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        prev_sum = 0
        print(nums)
        for R in range(2 * len(nums) - 1):
            print(f"R is {R} with value {nums[R % len(nums)]}")
            print(f"prev sum before {prev_sum}")
            prev_sum = max(prev_sum, 0)
            # print(f"prev sum after {prev_sum}")
            prev_sum += nums[R % len(nums)]
            # print(f"added {nums[R % len(nums)]} prev sum now {prev_sum}")
            max_sum = max(max_sum, prev_sum)
        return max_sum