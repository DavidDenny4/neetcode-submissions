class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        L, R = 0, len(nums) - 1

        while (L < R): 
            if nums[L] + nums[R] > target:
                R -= 1
            if nums[L] + nums[R] < target:
                L += 1
            if nums[L] + nums[R] == target:
                return [L,R]
        