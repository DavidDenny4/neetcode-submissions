class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        sum = 0
        min_length = len(nums) + 1
        for R in range(len(nums)):
            sum += nums[R]
            if sum >= target:
                while sum >= target:
                    length = R - L + 1
                    min_length = min(length, min_length)
                    sum -= nums[L]
                    L += 1
        if min_length == len(nums) + 1:
            return 0 
        else:
            return min_length

            