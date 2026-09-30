class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def helper(index):

            if index == len(nums) - 1:
                return [nums[index]]
            
            res = []
            perms_after = helper(index + 1)
            for p in perms_after:
                for i in range(len(p) + 1):
                    res.append(p.insert(nums[index], i))
            return res

        return helper(0) if nums else []