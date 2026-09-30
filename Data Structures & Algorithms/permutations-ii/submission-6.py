class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def helper(index):

            if index >= len(nums):
                return [[]]
            
            res = []
            perms = helper(index + 1)
            for p in perms:
                for i in range(0, len(p) + 1):
                    res.append(p.copy().insert(nums[index]))
            
            print(f" res is {res}")
            return res


        return helper(0)