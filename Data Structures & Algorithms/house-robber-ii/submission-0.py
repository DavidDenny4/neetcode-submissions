class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            rob_one, rob_two = 0, 0
            for n in nums:
                current_one = rob_one
                rob_one = rob_two
                rob_two = max(current_one + n, rob_two)
            return rob_two
        
        return max(helper(nums[:-1]), helper(nums[1:]))