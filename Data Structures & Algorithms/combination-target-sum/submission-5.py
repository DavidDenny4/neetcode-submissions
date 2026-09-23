class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(index, subset):
            if index >= len(nums):
                return 
            
            total = 0
            for n in subset:
                total += n
            if total == target:
                res.append(subset.copy())
                return 
            if total > target:
                return 
            subset.append(nums[index])
            helper(index, subset)
            subset.pop()
            helper(index + 1, subset)
        
        helper(0, [])
        return res
