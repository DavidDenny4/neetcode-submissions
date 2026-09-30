class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 0
        L = 0
        for R in range(len(nums)):
            print(f"nums is {nums}")
            print(f"BEFORE: L is {L} and R is {R}")
            while R < len(nums) and nums[R] == nums[L]:
                R += 1
            print(f"AFTER: L is {L} and R is {R}")
            nums[k] = nums[L]
            L = R
        return k