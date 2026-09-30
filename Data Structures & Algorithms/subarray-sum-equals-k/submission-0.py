class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        def helper(index, curr_sum):
            if index >= len(nums):
                return
            
            if curr_sum == k:
               res += 1

            curr_sum += nums[index]
            helper(index + 1, curr_sum.copy())
            curr_sum -= nums[index]
            helper(index + 1, curr_sum.copy())
        
        helper(0,0)
        return res