class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = 0
        L = 0
        for R in range(1, len(nums)):
            if nums[R] != nums[L]:
                count += 1
                L += 1
            else:
                while(nums[R] == nums[L]):
                    R += 1
                count += 1
                L = R
        return count