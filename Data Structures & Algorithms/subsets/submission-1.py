class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []

        def helper(index, subset):
            if index == len(nums):
                s = subset
                res.append(s)
                return
            
            subset.append(nums[index])
            helper(index + 1, subset)
            subset.pop()
            helper(index + 1, subset)
        
        helper(0, [])
        return res
