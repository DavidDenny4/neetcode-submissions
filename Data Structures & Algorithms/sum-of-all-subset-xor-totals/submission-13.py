class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        subset = []
        
        def helper(index, curr_set):
            if index == len(nums):
                subset.append(curr_set.copy())
                return
            
            curr_set.append(nums[index])
            helper(index + 1, curr_set)
            curr_set.pop()
            helper(index + 1, curr_set)
        
        helper(0, [])
        
        for sub in subset:
            xor_val = 0
            for val in sub:
                xor_val ^= val
            total += xor_val
        return total