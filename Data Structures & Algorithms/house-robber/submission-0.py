class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        last = length - 1
        second_last = length - 2
        cache = {}
        first_sum = rec(last, 0)
        second_sum = rec(second_last, 0)

        def rec(n, sum):
            sum += nums[n]
            if n >= 2:
                if (n - 2) in cache:
                    sum += cache[n - 2] 
                else:
                    rec(n - 2, sum)
            return sum

        return max(first_sum, second_sum)
