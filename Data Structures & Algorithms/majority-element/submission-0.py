class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_map = {}
        res, max_count = nums[0], 0
        for i in range(len(nums)):
            num_map[nums[i]] = nums_map.get(nums[i], 0) + 1 
            if num_map[nums[i]] > max_count:
                max_count = num_map[nums[i]]
                res = nums[i]
        return res