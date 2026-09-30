class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 0
        L = 0
        for R in range(len(nums)):
            while R < len(nums) and nums[R] == nums[L]:
                R += 1
            nums[k] = nums[L]
            L = R
        return k