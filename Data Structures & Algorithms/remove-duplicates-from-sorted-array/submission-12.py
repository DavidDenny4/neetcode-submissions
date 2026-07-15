class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        L, R = 0, 0
        while R < len(nums):
            while nums[R] == nums[L] and R < len(nums):
                R += 1
            nums[count] = nums[L]
            L = R
        return count