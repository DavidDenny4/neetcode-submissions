class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 0
        L = 0
        for R in range(len(nums)):
            print(f"original val of R is {R}")
            while R < len(nums) and nums[R] == nums[L]:
                R += 1
                print(f"R is now {R}")
            print(f"nums is {nums}")
            nums[k] = nums[L]
            L = R
        return k