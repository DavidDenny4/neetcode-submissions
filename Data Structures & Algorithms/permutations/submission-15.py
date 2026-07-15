class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def helper(index):

            if index == len(nums) - 1:
                return [[nums[index]]]
            
            res = []
            perms_after = helper(index + 1)
            print(f" perms after is {perms_after}")
            for p in perms_after:
                print(f"original array of p is {p}")
                for i in range(len(p) + 1):
                    print(f"i is {i}")
                    new_perm = p.copy()
                    new_perm.insert(i, nums[index])
                    print(f"new_perm is {new_perm}")
                    res.append(new_perm)
                    break
                break
            return res

        return helper(0) if nums else []