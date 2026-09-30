class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sorted_nums = nums.sort()
        sorted_dec_nums = nums.sort(reverse=True)

        if sorted_nums == nums or sorted_dec_nums == nums:
            return True
        return False