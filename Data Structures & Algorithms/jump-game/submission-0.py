class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        valid = [None] * len(nums)
        valid[len(valid) - 1] = True
        
        def dfs(index):
            if index == len(nums) - 1:
                valid[index] = True
                return True

            if valid[index] is not None:
                return valid[index]
            
            if dfs(index + nums[index]):
                valid[index] = True
                return True
            valid[index] = False
            return False

        return dfs(0)           
        