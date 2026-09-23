class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc_nums = nums.copy()
        desc_nums = nums.copy()
        asc_nums.sort()
        desc_nums.sort(reverse=True)  

        if asc_nums == nums or desc_nums == nums:
            return True
        return False