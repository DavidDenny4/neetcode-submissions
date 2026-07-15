class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(index, subset):
            if index >= len(nums):
                return 
            
            subset.append(nums[index])
            total = 0
            for n in subset:
                total += n
            if total == target:
                res.append(subset)
                return 
            helper(index + 1, subset)
            subset.pop()
            helper(index + 1, subset)
        
        return res
