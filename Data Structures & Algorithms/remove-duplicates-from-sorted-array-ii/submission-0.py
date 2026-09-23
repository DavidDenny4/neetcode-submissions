class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        L, R = 0, 0
        while R < len(nums):
            while R < len(nums) and nums[R] == nums[L] and (R - L + 1) <= 2:
                nums[count] = nums[L]
                count += 1
                R += 1
            while R < len(nums) and nums[R] == nums[L]:
                R += 1
            L = R
        return count