class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, max_sum = 0, nums[0]
        for num in nums:
            sum += num
            max_sum = max(max_sum, sum)
            if sum < 0:
                sum = 0
        return max_sum
            