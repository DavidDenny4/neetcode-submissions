class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and i == nums[i - 1]:
                continue
            
            L, R = i + 1, len(nums) - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    while (L + 1) < len(nums) and nums[L + 1] != nums[L]:
                        L += 1
        return res