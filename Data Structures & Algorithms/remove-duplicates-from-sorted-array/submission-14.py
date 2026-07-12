class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        L, R = 0, 0
        while R < len(nums):
            while R < len(nums) and nums[R] == nums[L]:
                R += 1
            nums[count] = nums[L]
            L = R
            count += 1
        return count