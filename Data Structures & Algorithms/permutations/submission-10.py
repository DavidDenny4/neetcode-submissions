class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def helper(index):

            if index == len(nums) - 1:
                return [[nums[index]]]
            
            res = []
            perms_after = helper(index + 1)
            for p in perms_after:
                for i in range(len(p) + 1):
                    new_perm = p.copy()
                    print(f"perm is {new_perm}")
                    new_perm.insert(nums[index], i)
                    print(f"perm is {new_perm}")
                    res.append(new_perm)
                    break
                break
            return res

        return helper(0) if nums else []