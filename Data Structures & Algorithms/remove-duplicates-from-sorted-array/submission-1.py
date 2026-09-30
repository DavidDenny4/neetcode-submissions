class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        nums = list(nums_set)
        return len(nums_set)