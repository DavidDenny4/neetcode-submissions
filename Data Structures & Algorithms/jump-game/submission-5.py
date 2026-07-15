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
            
            for jump in range(1, nums[index] + 1):
                if (index + jump) < len(nums) and dfs(index + jump):
                    valid[index] = True
                    return True
            return False

        return dfs(0)           
        