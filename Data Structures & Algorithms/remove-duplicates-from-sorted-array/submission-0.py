class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        return len(nums_set)