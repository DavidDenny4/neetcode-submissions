class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in nums_map:
                return [nums_map[compliment], i]
            nums_map[nums[i]] = i