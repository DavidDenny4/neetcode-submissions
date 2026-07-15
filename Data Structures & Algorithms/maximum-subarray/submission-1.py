class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        res = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > max + nums[i]:
                max = nums[i]
                res = [nums[i]]
            else:
                max += nums[i]
                res.append(nums[i])
        print(res)
        return max
            