class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            hash_map[nums[i]] = i
        
        for i in range(len(nums)):
            target_val = target - nums[i]
            if target_val in hash_map and hash_map[target_val] != i:
                return [i, hash_map[target_val]]
        
        return []