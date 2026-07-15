class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def helper(index):

            if index == len(nums) - 1:
                return [[nums[index]]]
            
            res = []
            perms_after = helper(index + 1)
            for p in perms_after:
                new_perm = p.copy()
                for i in range(len(p) + 1):
                    new_permp.insert(nums[index], i)
                    res.append(new_perm)
            return res

        return helper(0) if nums else []