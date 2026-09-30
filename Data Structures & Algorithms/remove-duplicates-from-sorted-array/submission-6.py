class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 0
        L = 0
        for R in range(len(nums)):
            index = R
            while index < len(nums) and nums[index] == nums[L]:
                index += 1
            nums[k] = nums[L]
            L = index
            R = index
        return k